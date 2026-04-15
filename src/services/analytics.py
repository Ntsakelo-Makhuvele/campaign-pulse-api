import pandas as pd

class AnalyticsService:
    def __init__(self):
        # Initialize any necessary resources, e.g., database connection
        pass

    def get_aggr_daily_performance(self, month: str =None):
        try:
            df = pd.read_csv('campaign_data.csv')
            df['date'] = pd.to_datetime(df['send_date'])
            df['week_day'] = df['date'].dt.day_name()
            df['month'] = df['date'].dt.month_name()
            mask = pd.Series([True] * len(df))
            if month:
                mask &= (df['month'] == month)
            filtered_df = df[mask] 
            campaign_performance = filtered_df.groupby('week_day').agg({
                'impressions': 'sum',
                'conversions': 'sum'
            }).reset_index()
            return campaign_performance
        except Exception as e:
            return {"error":str(e)}

    