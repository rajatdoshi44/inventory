from fastapi import FastAPI
from services.company.router import router

app = FastAPI(title="Company Service", version="1.0.0")
app.include_router(router)

