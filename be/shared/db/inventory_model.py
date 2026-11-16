from shared.db.database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Float
from pgvector.sqlalchemy import Vector
from sqlalchemy.orm import relationship

class Inventory(Base):
    __tablename__ = "INVENTORY"

    product_id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, nullable=False)
    product_description = Column(String, nullable=True)
    product_price = Column(Float, nullable=False)
    product_quantity = Column(Integer, nullable=False)
    product_model = Column(String, nullable=True)
    currency = Column(String, nullable=False)
    company_id = Column(Integer, ForeignKey("COMPANY.company_id"), nullable=False)
    embedding = Column(Vector(768), nullable=True)  # Assuming embedding is a float; adjust type as needed


    company = relationship("Company", back_populates="inventories")