from pydantic import BaseModel
from decimal import Decimal
from typing import Optional

class EmailBenchmark(BaseModel):
    ctr: Decimal
    unique_clicks: int
    unique_opens: int

class PushBenchmark(BaseModel):
    opr: Decimal
    unique_opens: int

class InappBenchmark(BaseModel):
    itr: Decimal
    unique_clicks: int
    impressions: int


class BenchmarkOptions(BaseModel):
    is_ctr: Optional[bool] = False
    is_unique_clicks: Optional[bool] = False
    is_unique_opens: Optional[bool] = False
    is_impressions: Optional[bool] = False
    is_opr: Optional[bool] = False
    is_itr: Optional[bool] = False


