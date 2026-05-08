# DataMonitor

콘솔 기반 실시간 데이터 모니터링 관리자 도구.
주문 상태별 현황과 시료별 재고 수량을 일정 주기로 자동 갱신하여 터미널에 표시합니다.

## 기능

### 주문 현황
- 전체 주문을 4단계 상태별로 분류하여 조회
- 상태별 건수 요약 및 상세 목록 표시

| 상태 | 설명 |
|------|------|
| `RESERVED` | 예약 접수 완료 |
| `CONFIRMED` | 주문 확정 |
| `PRODUCING` | 생산 진행 중 |
| `RELEASE` | 출고 완료 |

### 재고 현황
- 시료(sample) 단위로 현재 재고 수량 조회
- 전체 시료 목록을 표 형식으로 표시

### 실시간 갱신
- 5초 주기로 데이터를 다시 읽어 화면 자동 갱신
- `Ctrl+C`로 종료

## 프로젝트 구조

```
datamonitor/
├── main.py              # 진입점: 메인 루프 + render()
├── config.py            # 경로 설정
├── display.py           # 콘솔 출력 유틸
├── views/
│   ├── orders.py        # 주문 조회 로직
│   └── inventory.py     # 재고 조회 로직
├── data/
│   ├── orders.json      # 주문 데이터
│   └── inventory.json   # 재고 데이터
└── tests/
    ├── conftest.py
    ├── test_orders.py
    ├── test_inventory.py
    └── test_display.py
```

## 데이터 형식

**data/orders.json**
```json
{
  "ORD-001": {
    "status": "RESERVED",
    "sample": "SMP-A",
    "quantity": 5,
    "created_at": "2026-05-07"
  }
}
```

**data/inventory.json**
```json
{
  "SMP-A": { "quantity": 85 }
}
```

## 실행 방법

```bash
uv run python main.py
```

## 테스트

```bash
uv run pytest tests/ -v
```

## 요구사항

- Python >= 3.14
- uv
