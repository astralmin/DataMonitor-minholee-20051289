import sys
import json
import pytest

sys.path.insert(0, r"C:\reviewer\project\datapersistence")


@pytest.fixture
def orders_file(tmp_path):
    data = {
        "ORD-001": {"status": "RESERVED",  "sample": "SMP-A", "quantity": 5,  "created_at": "2026-05-07"},
        "ORD-002": {"status": "CONFIRMED", "sample": "SMP-B", "quantity": 3,  "created_at": "2026-05-07"},
        "ORD-003": {"status": "PRODUCING", "sample": "SMP-A", "quantity": 10, "created_at": "2026-05-06"},
        "ORD-004": {"status": "RELEASE",   "sample": "SMP-C", "quantity": 2,  "created_at": "2026-05-05"},
    }
    f = tmp_path / "orders.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    return str(f)


@pytest.fixture
def inventory_file(tmp_path):
    data = {
        "SMP-A": {"quantity": 85},
        "SMP-B": {"quantity": 42},
        "SMP-C": {"quantity": 198},
    }
    f = tmp_path / "inventory.json"
    f.write_text(json.dumps(data), encoding="utf-8")
    return str(f)
