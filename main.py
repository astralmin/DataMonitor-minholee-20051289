import time
import sys

import config  # json_store 임포트 전 sys.path 주입 필수
from views.orders import OrderView, ORDER_STATUSES
from views.inventory import InventoryView
import display


def render() -> None:
    order_view = OrderView()
    inventory_view = InventoryView()

    display.clear()
    print(f"  DataMonitor  |  {display.now()}  |  종료: Ctrl+C\n")

    # 주문 요약
    print(display.section("주문 현황 요약"))
    summary = order_view.get_summary()
    print(display.table(
        [(s, 12) for s in ORDER_STATUSES],
        [[str(summary[s]) for s in ORDER_STATUSES]],
    ))
    print()

    # 상태별 주문 목록
    for status in ORDER_STATUSES:
        orders = order_view.get_by_status(status)
        print(f"  [{status}]  {len(orders)}건")
        if orders:
            cols = [("주문ID", 12), ("시료", 10), ("수량", 6), ("접수일", 12)]
            rows = [
                [oid, o.get("sample", "-"), o.get("quantity", "-"), o.get("created_at", "-")]
                for oid, o in orders.items()
            ]
            print(display.table(cols, rows))
        print()

    # 재고 현황
    print(display.section("재고 현황"))
    inventory = inventory_view.get_all()
    if inventory:
        cols = [("시료ID", 16), ("현재 재고", 10)]
        rows = [[sid, info.get("quantity", "-")] for sid, info in inventory.items()]
        print(display.table(cols, rows))
    else:
        print("  (데이터 없음)")
    print()


def main() -> None:
    try:
        while True:
            render()
            time.sleep(config.REFRESH_INTERVAL)
    except KeyboardInterrupt:
        display.clear()
        print("DataMonitor 종료.")
        sys.exit(0)


if __name__ == "__main__":
    main()
