from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from shared.db.database import get_db
from shared.api.response import APIResponse
from services.company.model import create_company_model, get_companies_list_model
from services.company.type import CompanyCreateRequest, CompanyCreateResponse, CompaniesListResponse, CompaniesListRequest

router = APIRouter()

@router.post('/create-company', response_model=APIResponse[CompanyCreateResponse])
def create_company(company_data: CompanyCreateRequest, db: Session = Depends(get_db)):
 return create_company_model(company_data, db)

@router.post("/company-list", response_model=APIResponse[CompaniesListResponse | None])
def get_companies_list(payload: CompaniesListRequest,db: Session = Depends(get_db)):
   return get_companies_list_model(payload,db)

@router.post("/health", response_model=APIResponse[dict])
def health_check(db: Session = Depends(get_db)):
    try:
        # Perform a simple database query to check connectivity
        db.execute("SELECT 1")
        return APIResponse(data={"status": "healthy"}, status=200, msg="Service is healthy")
    except Exception as e:
        return APIResponse(data=None, status=500, msg=f"Service is unhealthy: {str(e)}")