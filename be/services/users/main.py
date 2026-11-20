from fastapi import FastAPI

from services.users.router import router

app = FastAPI(title="Users Service", version="1.0.0")
app.include_router(router)
