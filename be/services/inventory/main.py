from services.inventory.router import router
from fastapi import FastAPI

app = FastAPI(title="Inventory Service", version="1.0.0")
app.include_router(router, prefix="/inventory")