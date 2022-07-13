from dataclasses import dataclass, field
from sqlalchemy import Column, Integer, String, Numeric, null


from .base import Base


class SyncEventModel(Base):
    __tablename__ = "syncevent"

    reserve0 = Column(Numeric, nullable=False)
    reserve1 = Column(Numeric, nullable=False)
    hash = Column(String, nullable=False)
    block_number = Column(Numeric, nullable=False)
    transaction_index = Column(Integer, nullable=False)
    pair_address = Column(String, nullable=False)
    method = Column(String, nullable=False)
