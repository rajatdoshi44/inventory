from shared.api.response import APIResponse
from shared.db.company_model import Company

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
    except Exception as e:
        return APIResponse(data=None, status=500, msg=f"Failed to create company: {str(e)}")
    