import json
import pytest
from views.inventory import InventoryView


def test_get_all_returns_all_samples(inventory_file, monkeypatch):
    monkeypatch.setattr("views.inventory.INVENTORY_FILE", inventory_file)
    result = InventoryView().get_all()
    assert set(result.keys()) == {"SMP-A", "SMP-B", "SMP-C"}


def test_get_all_quantity_values(inventory_file, monkeypatch):
    monkeypatch.setattr("views.inventory.INVENTORY_FILE", inventory_file)
    result = InventoryView().get_all()
    assert result["SMP-A"]["quantity"] == 85
    assert result["SMP-B"]["quantity"] == 42
    assert result["SMP-C"]["quantity"] == 198


def test_get_all_empty_store(tmp_path, monkeypatch):
    f = tmp_path / "empty.json"
    f.write_text(json.dumps({}), encoding="utf-8")
    monkeypatch.setattr("views.inventory.INVENTORY_FILE", str(f))
    assert InventoryView().get_all() == {}
