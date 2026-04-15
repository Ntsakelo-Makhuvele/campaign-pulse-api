from fastapi import APIRouter,HTTPException,status
from src.services.analytics import AnalyticsService

analytics_router = APIRouter()
analytics_service = AnalyticsService()

@analytics_router.get("/analytics/weekday_performance")
def campaign_weekday_performance(month: str = None):
    try:
        result = analytics_service.get_aggr_daily_performance(month)
        if result.empty:
            raise HTTPException(status_code=status.HTTP_204_NO_CONTENT, detail={"error":f"{result}"})
        else:
            return result.to_dict(orient='records')
    except Exception as e:
         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error":f"{e}"})
