from fastapi import APIRouter,HTTPException,status
from src.services.analytics import AnalyticsService
from src.schemas.Analytics import BenchmarkOptions,EmailBenchmark, PushBenchmark, InappBenchmark
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

@analytics_router.get('/analytics/top_n_emails/{limit}')
def top_n_emails(limit:int,benchmark:EmailBenchmark, benchmarkOptions:BenchmarkOptions,month:str=None):
    try:
        email_df = analytics_service.top_n_performing_emails(benchmark,benchmarkOptions,limit, month)
        return email_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"HTTPError":str(e)}) 

@analytics_router.get('/analytics/top_n_pushes/{limit}')
def top_n_push(limit:int,benchmark:PushBenchmark, benchmarkOptions:BenchmarkOptions,month:str=None):
    try:
        push_df = analytics_service.top_n_performing_pushes(benchmark,benchmarkOptions,limit, month)
        return push_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"HTTPError":str(e)})

@analytics_router.get('/analytics/top_n_inapps/{limit}')
def top_n_inapp(limit:int,benchmark:InappBenchmark, benchmarkOptions:BenchmarkOptions,month:str=None):
    try:
        inapp_df = analytics_service.top_n_performing_inapps(benchmark,benchmarkOptions,limit, month)
        return inapp_df.to_dict(orient="records")
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail={"HTTPError":str(e)}) 
    

