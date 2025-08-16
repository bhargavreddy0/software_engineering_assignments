from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import conf
from urllib.parse import quote_plus

# Build a safe connection string for pymysql
password = quote_plus(conf.password or "")
SQLALCHEMY_DATABASE_URL = (
    f"mysql+pymysql://{conf.user}:{password}@{conf.host}:{conf.port}/{conf.database}"
    "?charset=utf8mb4"
)

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
