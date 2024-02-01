from datetime import datetime

from pydantic import BaseModel


class APIExchangeRate(BaseModel):
    disclaimer: str
    license: str
    timestamp: datetime
    base: str
    rates: dict[str, float]
