from fastapi import APIRouter,Depends
from requests import Session
from shared.db.database import get_db
from services.inventory.type import CreateInventoryRequest, CreateInventoryResponse, InventoryListRequest, InventoryListResponse
from services.inventory.model import create_inventory_model, inventory_semantic_search_model, list_inventory_model
from shared.api.response import APIResponse
router = APIRouter()

@router.post("/create", response_model=APIResponse[CreateInventoryResponse | None])
async def create_inventory(item: CreateInventoryRequest, db: Session = Depends(get_db)):
  return create_inventory_model(item, db)

@router.post("/list", response_model=APIResponse[InventoryListResponse|None])
async def list_inventory(payload:InventoryListRequest, db: Session = Depends(get_db)):
    return list_inventory_model(payload, db)

@router.post("/semantic-search", response_model=APIResponse[list[CreateInventoryResponse]|None])
async def semantic_search(payload: InventoryListRequest, db: Session = Depends(get_db)):
    return inventory_semantic_search_model(payload, db)

@router.get("/health")
async def health_check():
    return {"status": "healthy"}