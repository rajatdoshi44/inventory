import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# .env से DATABASE_URL लेगा, नहीं मिलने पर डॉकर वाला डिफ़ॉल्ट URL इस्तेमाल करेगा
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://admin:admin123@localhost:5432/ai_inventory_db"
)

# SQLAlchemy Engine
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Database Dependency (सभी सर्विसेस के API राउट्स के लिए)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

