from shared.db.database import engine
from shared.db.inventory_model import Inventory
from shared.db.company_model import Company

def create_tables() -> None:
    Inventory.metadata.create_all(bind=engine)
    Company.metadata.create_all(bind=engine)

def drop_tables() -> None:
    Inventory.metadata.drop_all(bind=engine)
    Company.metadata.drop_all(bind=engine)

if __name__ == "__main__":
    create_tables()