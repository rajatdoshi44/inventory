from services.inventory.type import CreateInventoryRequest, CreateInventoryResponse, InventoryListRequest, Inventory as InventoryData, InventoryListResponse
from requests import Session
from shared.db.inventory_model import Inventory
from shared.api.response import APIResponse
from shared.llm.model import llm_model_generate_embedding
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError
from shared.db.company_model import Company

def create_inventory_model(item: CreateInventoryRequest, db: Session):
    try:
        # Create a new inventory instance
        company = db.query(Company).where(Company.company_id == item.company_id).first()
        if not  company:
         return APIResponse(data=None, status=200, msg="Company not found")
               
        contents = f"Product Name: {item.product_name}, Product Description: {item.product_description}, Product model: {item.product_model}, Company Name: {Company.company_name}"
        embedding = llm_model_generate_embedding(
            contents=contents,
            task_type="RETRIEVAL_DOCUMENT",
        )
        new_inventory = Inventory(**item.model_dump(), embedding=embedding)
        
        # Add the new inventory to the session and commit
        db.add(new_inventory)
        db.commit()
        db.refresh(new_inventory)
        return APIResponse(data=CreateInventoryResponse(product_id=new_inventory.product_id, product_name=new_inventory.product_name), status=200, msg="Inventory created successfully")
    except IntegrityError as e:
        db.rollback()  # Mandatory: reset the failed transaction
        error_detail = str(e.orig)
        return APIResponse(data=None, status=500, msg=f"An error occurred: {str(error_detail)}")
    except Exception as e:
        db.rollback()
        return APIResponse(data=None, status=500, msg=f"An error occurred: {str(e)}")
    # Implementation for creating inventory model

def list_inventory_model(payload: InventoryListRequest, db: Session):
    try:
        total_rows = db.query(Inventory).count()
        # Calculate offset for pagination
        offset = (payload.page - 1) * payload.limit
        
        # Query the database for inventory items with pagination
        inventory_items = db.query(Inventory).offset(offset).limit(payload.limit).all()
        
        # Prepare the response data
        response_data = [
            InventoryData.model_validate(item, from_attributes=True) 
            for item in inventory_items
        ]
        
        return APIResponse(data=InventoryListResponse(total_records=total_rows, data=response_data), status=200, msg="Inventory list retrieved successfully")
    except Exception as e:
        return APIResponse(data=None, status=500, msg=f"An error occurred: {str(e)}")

def inventory_semantic_search_model(payload: InventoryListRequest, db: Session):
    try:
        embedding = llm_model_generate_embedding(
            contents=payload.search_query,
            task_type="RETRIEVAL_QUERY",
        )
        cosine_distance = Inventory.embedding.cosine_distance(embedding).label("distance")
        stmt = (
            select(Inventory, cosine_distance)
            .where(Inventory.embedding.is_not(None))
            .where(cosine_distance < 0.45)
            .order_by(cosine_distance)
            .limit(payload.limit)
        )
        results = db.execute(stmt).all()
        response_data = [CreateInventoryResponse(product_id=item.Inventory.product_id, product_name=item.Inventory.product_name, cosine_distance=item.distance) for item in results]   
        return APIResponse(data=response_data, status=200, msg="Inventory semantic search results retrieved successfully")
    except Exception as e:
        raise APIResponse(data=None, status=500, msg=f"An error occurred: {str(e)}")