from pydantic import BaseModel


class CreateInventoryRequest(BaseModel):
    product_name: str

class CreateInventoryResponse(BaseModel):
    product_id: int
    product_name: str
    cosine_distance: float | None = None


class InventoryListRequest(BaseModel):
    search_query: str
    page: int
    limit: int  