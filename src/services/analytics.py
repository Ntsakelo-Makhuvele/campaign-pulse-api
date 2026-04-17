import pandas as pd
from src.schemas.Analytics import Benchmark

class AnalyticsService:
    def __init__(self):
       pass
    def read_data(self,channel: str):
        try:
            if channel == 'email':
                df = pd.read_csv('campaign_pulse_email_v1.csv')
               #df = pd.read_csv('campaign_data_v2.csv')
            if channel == 'push':
               df = pd.read_csv('campaign_pulse_push_v1.csv')
            if channel == 'in-app':
               df = pd.read_csv('campaign_pulse_inapp_v1.csv')   
            df['send_time'] = pd.to_datetime(df['send_time'], format='%Y-%m-%d %H:%M')
            df['week_day'] = df['send_time'].dt.day_name()
            df['month'] = df['send_time'].dt.month_name()
            return df
        except Exception as e:
            return {"error":str(e)}
  
    def get_aggr_daily_performance_emails(self, month: str =None):
        try:
            df = self.read_data(channel="email")
            mask = pd.Series([True] * len(df))
            if month:
                mask &= (df['month'] == month)
            filtered_df = df[mask] 
            campaign_performance = filtered_df.groupby('week_day').agg({
                'deliveries': 'sum',
                'unique_opens': 'sum',
                'unique_clicks': 'sum'
            }).reset_index()
            return campaign_performance
        except Exception as e:
            return {"error":str(e)}
        
    def get_aggr_daily_performance_push(self,month:str =None):
        try:
            df = self.read_data(channel='push')
            mask = pd.Series([True] * len(df))
            if month:
                mask &= (df['month'] == month)
            filtered_df = df[mask] 
            campaign_performance = filtered_df.groupby('week_day').agg({
                'deliveries': 'sum',
                'opens': 'sum'
            }).reset_index()
            return campaign_performance
        except Exception as e:
            return {"error": str(e)}
        
        
    def get_aggr_daily_performance_inapp(self,month:str =None):
        try:
            df = self.read_data(channel='in-app')
            mask = pd.Series([True] * len(df))
            if month:
                mask &= (df['month'] == month)
            filtered_df = df[mask] 
            campaign_performance = filtered_df.groupby('week_day').agg({
                'impressions': 'sum',
                'clicks': 'sum'
            }).reset_index()
            return campaign_performance
        except Exception as e:
            return {"error": str(e)}
        

    



    