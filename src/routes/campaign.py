from fastapi import APIRouter
from src.services.campaign import CampaignService
from src.schemas.campaign import Campaign

campain_router = APIRouter()
campaign_service = CampaignService()

@campain_router.post("/campaigns")
def add_campaign(campaign: Campaign):
    result = campaign_service.campaign_performance(campaign)
    return result