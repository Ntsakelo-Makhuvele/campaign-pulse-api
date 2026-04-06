from src.schemas.campaign import Campaign

class CampaignService:
    def __init__(self):
        self.campaigns = []

    def add_campaign(self, campaign: Campaign):
        self.campaigns.append(campaign)

    def get_campaigns(self):
        return self.campaigns
    
    def campaign_performance(self, campaign:Campaign):  
          try:
              ctr = (campaign.clicks / campaign.impressions) * 100 if campaign.impressions > 0 else 0
              conversion_rate = (campaign.conversions / campaign.clicks) * 100 if campaign.clicks > 0 else 0
              open_rate = (campaign.deliveries / campaign.impressions) * 100 if campaign.impressions > 0 else 0
              total_reach = campaign.deliveries
              return {
                    "ctr": ctr,
                    "conversion_rate": conversion_rate,
                    "open_rate": open_rate,
                    "total_reach": total_reach
              }          
          except Exception as e:
              return {"error": str(e)}
   