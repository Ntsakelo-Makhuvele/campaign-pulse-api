from pydantic import BaseModel

class Benchmark(BaseModel):
    metric: str
    target: int