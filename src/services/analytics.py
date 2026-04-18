import pandas as pd
from src.schemas.Analytics import EmailBenchmark, BenchmarkOptions,PushBenchmark, InappBenchmark

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
        

    def top_n_performing_emails(self,benchmark:EmailBenchmark, benchmarkOptions: BenchmarkOptions,limit:int = 5,month:str = None):
        try:
            df = self.read_data(channel='email')
            df["ctr"] = (df["unique_clicks"]/df["deliveries"]) * 100
            mask = pd.Series([True] * len(df))
            
            checked_options = []
            
            if month:
                mask &= (df["month"] == month)

            if benchmarkOptions.is_ctr:
                checked_options.append('ctr')
                mask &= (df["ctr"] >= benchmark.ctr)
            
            if benchmarkOptions.is_unique_clicks:
                checked_options.append('unique_clicks')
                mask &= (df["unique_clicks"] >= benchmark.unique_clicks)
            
            if benchmarkOptions.is_unique_opens:
                checked_options.append('unique_opens')
                mask &= (df["unique_opens"] >= benchmark.unique_opens)
            
            filtered_df = df[mask]
            top_n = filtered_df.nlargest(limit, checked_options)
            return top_n
        except Exception as e:
            return {"error":str(e)}
    
    def top_n_performing_pushes(self,benchmark:PushBenchmark, benchmarkOptions: BenchmarkOptions,limit:int = 5,month:str = None):
        try:
            df = self.read_data(channel="push")
            df["opr"] = (df["opens"]/df["deliveries"]) * 100
            mask = pd.Series([True] * len(df))
            checked_options = []
            if month:
                mask &= (df["month"] == month)

            if benchmarkOptions.is_opr:
                checked_options.append('opr')
                mask &= (df["opr"] >= benchmark.opr)
            
            if benchmarkOptions.is_unique_opens:
                checked_options.append('opens')
                mask &= (df["opens"] > benchmark.unique_opens)
            
            filtered_df = df[mask]

            top_n = filtered_df.nlargest(limit,checked_options)
            return top_n
        except Exception as e:
            return {"error": str(e)}

    def top_n_performing_inapps(self,benchmark:InappBenchmark, benchmarkOptions: BenchmarkOptions,limit:int = 5,month:str = None):
        try:
           df = self.read_data(channel="in-app")
           df["itr"] = (df["clicks"]/df["impressions"]) * 100
           mask = pd.Series([True] * len(df))
           checked_options = []

           if month:
               mask &= (df["month"] == month)
           
           if benchmarkOptions.is_unique_clicks:
               checked_options.append('clicks')
               mask &= (df["clicks"] >= benchmark.unique_clicks)
            
           if benchmarkOptions.is_impressions:
               checked_options.append('impressions')
               mask &= (df["impressions"] >= benchmark.impressions)

           if benchmarkOptions.is_itr:
               checked_options.append('itr')
               mask &= (df["itr"] >= benchmark.itr)

           filtered_df = df[mask]

           top_n = filtered_df.nlargest(limit, checked_options)
           return top_n 
        except Exception as e:
            return {"error": str(e)}






    