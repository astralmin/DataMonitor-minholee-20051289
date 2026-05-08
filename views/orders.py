from json_store import JsonStore
from config import ORDERS_FILE

ORDER_STATUSES = ["RESERVED", "CONFIRMED", "PRODUCING", "RELEASE"]


class OrderView:
    def __init__(self):
        self.store = JsonStore(ORDERS_FILE)

    def get_all(self) -> dict:
        return self.store.read_all()

    def get_by_status(self, status: str) -> dict:
        return {k: v for k, v in self.store.read_all().items() if v.get("status") == status}

    def get_summary(self) -> dict[str, int]:
        summary = {s: 0 for s in ORDER_STATUSES}
        for order in self.store.read_all().values():
            s = order.get("status")
            if s in summary:
                summary[s] += 1
        return summary
