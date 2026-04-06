from pydantic import BaseModel

class Campaign(BaseModel):
    id: int
    name: str
    impressions: int
    clicks: int
    conversions: int
    category: str
    start_date: str
    channel: str
    audience: str
    deliveries: int
   