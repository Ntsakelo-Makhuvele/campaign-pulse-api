from fastapi import APIRouter,HTTPException,status
from src.services.analytics import AnalyticsService
from pandas import DataFrame
analytics_router = APIRouter()
analytics_service = AnalyticsService()

@analytics_router.get("/analytics/weekday_performance")
def campaign_weekday_performance(month: str = None):
    try:
        final_data = {}
      
        email_df = analytics_service.get_aggr_daily_performance_emails(month)
        final_data["email"] = email_df.to_dict(orient="records") 
    
        push_df = analytics_service.get_aggr_daily_performance_push(month) 
        final_data["push"] = push_df.to_dict(orient="records")
  
        inapp_df = analytics_service.get_aggr_daily_performance_inapp(month) 
        final_data["in-app"] = inapp_df.to_dict(orient="records")
        
        return final_data
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail={"error":f"{e}"})
        