from pydantic import BaseModel


class CreateInventoryRequest(BaseModel):
    product_name: str
    product_description : str
    product_price : float
    product_quantity :int
    product_model : str
    currency : str
    company_id : int

class CreateInventoryResponse(BaseModel):
    product_id: int
    product_name: str
    product_description : str
    product_price : float
    product_quantity :int
    product_model : str
    currency : str
    company_id : int
    cosine_distance: float | None = None


class InventoryListRequest(BaseModel):
    search_query: str
    page: int
    limit: int  