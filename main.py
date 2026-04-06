from fastapi import FastAPI
from src.routes.campaign import campain_router
from src.database.database import db_init
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    print(f"server is starting...")
    try:
        db_init()
        print(f"Database initialized succesfully") 
    except Exception as e:
        print(f"Database initialization failed: {e}")
        raise
    yield
    print(f"server is shutting down...")

app = FastAPI(
    title="CampaignPulse API", 
    description="API for CampaignPulse application", 
    version="1.0.0",
    lifespan=lifespan
    )

app.include_router(router=campain_router, prefix="/api/v1", tags=["Campaigns"])


