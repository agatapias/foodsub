from fastapi import FastAPI
from routes import router
from database import engine
from models import Base

app = FastAPI()

app.include_router(router)

@app.get("/")
async def root():
    return {"message": "User Service is running"}

# Create tables on startup
@app.on_event("startup")
async def on_startup():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)