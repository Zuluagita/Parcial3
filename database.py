from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)



DATABASE_URL = f"postgresql://u5hzryszvsfwihhna1qs:3kJm20mPAfTcEbsSHCliSVXsQOiB8r@bbexxwo0eqot2cwljxae-postgresql.services.clever-cloud.com:50013/bbexxwo0eqot2cwljxae"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()