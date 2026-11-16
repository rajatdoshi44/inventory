from fastapi import FastAPI
from services.company.router import router

app = FastAPI()
app.include_router(router)

