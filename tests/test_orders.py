import json
import pytest
from views.orders import OrderView, ORDER_STATUSES


def test_order_statuses_order():
    assert ORDER_STATUSES == ["RESERVED", "CONFIRMED", "PRODUCING", "RELEASE"]


def test_get_all(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    assert len(OrderView().get_all()) == 4


def test_get_by_status_filters_correctly(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    result = OrderView().get_by_status("RESERVED")
    assert list(result.keys()) == ["ORD-001"]
    assert result["ORD-001"]["status"] == "RESERVED"


def test_get_by_status_returns_only_matching(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    for status in ORDER_STATUSES:
        result = OrderView().get_by_status(status)
        assert all(v["status"] == status for v in result.values())


def test_get_by_status_unknown_returns_empty(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    assert OrderView().get_by_status("UNKNOWN") == {}


def test_get_summary_counts(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    summary = OrderView().get_summary()
    assert summary == {"RESERVED": 1, "CONFIRMED": 1, "PRODUCING": 1, "RELEASE": 1}


def test_get_summary_all_statuses_present(orders_file, monkeypatch):
    monkeypatch.setattr("views.orders.ORDERS_FILE", orders_file)
    assert set(OrderView().get_summary().keys()) == set(ORDER_STATUSES)


def test_get_summary_empty_store(tmp_path, monkeypatch):
    f = tmp_path / "empty.json"
    f.write_text(json.dumps({}), encoding="utf-8")
    monkeypatch.setattr("views.orders.ORDERS_FILE", str(f))
    summary = OrderView().get_summary()
    assert all(v == 0 for v in summary.values())
