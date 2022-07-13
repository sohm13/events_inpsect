from pydantic import BaseModel


class Pair(BaseModel):
    address: str
    symbol: str
