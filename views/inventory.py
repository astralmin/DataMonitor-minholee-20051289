from json_store import JsonStore
from config import INVENTORY_FILE


class InventoryView:
    def __init__(self):
        self.store = JsonStore(INVENTORY_FILE)

    def get_all(self) -> dict:
        return self.store.read_all()
