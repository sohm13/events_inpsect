import os
from sqlalchemy import create_engine, orm
from sqlalchemy.orm import sessionmaker




def get_sync_evenet_db_uri():
    username = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    db_name = "inpsect_sync"
    return f"postgresql+psycopg2://{username}:{password}@{host}/{db_name}"


def _get_engine(uri: str):
    return create_engine(
        uri,
        executemany_mode="values",
        executemany_values_page_size=10000,
        executemany_batch_page_size=500,
    )

def _get_sessionmaker(uri: str):
    return sessionmaker(bind=_get_engine(uri))


def get_inspect_sessionmaker():
    uri = get_sync_evenet_db_uri()
    return _get_sessionmaker(uri)


def get_inspect_session() -> orm.Session:
    Session = get_inspect_sessionmaker()
    return Session()