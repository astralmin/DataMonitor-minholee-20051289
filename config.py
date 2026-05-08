import sys
import os

CRUD_LIB_PATH = r"C:\reviewer\project\datapersistence"
if CRUD_LIB_PATH not in sys.path:
    sys.path.insert(0, CRUD_LIB_PATH)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")
os.makedirs(DATA_DIR, exist_ok=True)

ORDERS_FILE = os.path.join(DATA_DIR, "orders.json")
INVENTORY_FILE = os.path.join(DATA_DIR, "inventory.json")

REFRESH_INTERVAL = 5  # 초
