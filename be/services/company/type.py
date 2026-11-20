from pydantic import BaseModel, ConfigDict

class CompanyCreateRequest(BaseModel):
    company_name: str
    company_description: str = None
    company_address: str = None
    company_email: str = None
    company_phone: str = None
    company_gst_number: str = None
    company_pan_number: str = None
    company_website: str = None
    company_logo_url: str = None
    company_status: str = None
    company_cin_number: str = None
    company_industry: str = None

class CompanyCreateResponse(BaseModel):
    company_id: int
    company_name: str
    company_description: str = None
    company_address: str = None
    company_email: str = None
    company_phone: str = None
    company_gst_number: str = None
    company_pan_number: str = None
    company_website: str = None
    company_logo_url: str = None
    company_status: str = None
    company_cin_number: str = None
    company_industry: str = None

class Companies(BaseModel):
    model_config = ConfigDict(from_attributes=True) 
    company_id: int
    company_name: str
    company_description: str = None
    company_address: str = None
    company_email: str = None
    company_phone: str = None
    company_gst_number: str = None
    company_pan_number: str = None
    company_website: str = None
    company_logo_url: str = None
    company_status: str = None
    company_cin_number: str = None
    company_industry: str = None

class CompaniesListResponse(BaseModel):
    total_companies:int
    data: list[Companies]

class CompaniesListRequest(BaseModel):
    limit:int
    page_number: int