

from shared.db.database import Base
from shared.db.inventory_model import Inventory
from sqlalchemy import Column, Integer, String, func, DateTime
from sqlalchemy.orm import relationship


class Company(Base):
    __tablename__ = "COMPANY"

    company_id = Column(Integer, primary_key=True, index=True)
    company_name = Column(String, nullable=False)
    company_description = Column(String, nullable=True)
    company_address = Column(String, nullable=True)
    company_email = Column(String, nullable=True)
    company_phone = Column(String, nullable=True)
    company_gst_number = Column(String, nullable=True)
    company_pan_number = Column(String, nullable=True)
    company_website = Column(String, nullable=True)
    company_logo_url = Column(String, nullable=True)
    company_status = Column(String, nullable=True)  # e.g., active, inactive
    company_updated_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    company_created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    company_cin_number = Column(String, nullable=True)  # Corporate Identification Number
    company_industry = Column(String, nullable=True)  # Industry type
    
    inventories = relationship(
        Inventory, back_populates="company", cascade="all, delete-orphan"
    )