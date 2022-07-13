from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer


class Base:

    id = Column(Integer, primary_key=True)
    
    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)
