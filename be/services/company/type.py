from pydantic import BaseModel

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