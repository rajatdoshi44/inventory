from shared.api.response import APIResponse
from shared.db.company_model import Company
from sqlalchemy.exc import IntegrityError
from services.company.type import CompaniesListResponse
from sqlalchemy import func

def create_company_model(company_data, db) -> APIResponse[dict]:
    try:
        company_model = Company(
            company_name=company_data.company_name,
            company_description=company_data.company_description,
            company_address=company_data.company_address,
            company_email=company_data.company_email,
            company_phone=company_data.company_phone,
            company_gst_number=company_data.company_gst_number,
            company_pan_number=company_data.company_pan_number,
            company_website=company_data.company_website,
            company_logo_url=company_data.company_logo_url,
            company_status=company_data.company_status,
            company_cin_number=company_data.company_cin_number,
            company_industry=company_data.company_industry
        )
        db.add(company_model)
        db.commit()
        db.refresh(company_model)

        return APIResponse(data={"company_id": company_model.company_id}, status=200, msg="Company created successfully")
    
    except IntegrityError as e:
        db.rollback()
        return APIResponse(data=None, status=400, msg=f"Integrity error: {str(e.orig)}")
    except Exception as e:
        return APIResponse(data=None, status=500, msg=f"Failed to create company: {str(e)}")


def get_companies_list_model(payload,db)->APIResponse[CompaniesListResponse | None]:
    try:
        page = payload.page_number
        page_size = payload.limit
        offset = (page - 1) * page_size
        base_query= db.query(Company)
        response = base_query.order_by(Company.company_id.asc()).offset(offset).limit(page_size).all()
        total_companies = base_query.with_entities(func.count(Company.company_id)).scalar()
        
        return APIResponse(data= CompaniesListResponse(total_companies=total_companies, data=response), status=200, msg="Successfully retrieved companies.")
    except Exception as e:
        return APIResponse(data= None, status=500, msg=str(e))