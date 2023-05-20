from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = "oracle.fiap.com.br"
DB_PORT = 1521
DB_SERVICE_NAME = "ORCL"

DB_USERNAME = "USER"
DB_PASSWORD = "PASSWORD"


def get_engine_session():
    engine = create_engine(
        f"oracle+cx_oracle://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_SERVICE_NAME}"
    )
    session = sessionmaker(bind=engine)()

    return engine, session
