# DataMonitor

콘솔 기반 실시간 데이터 모니터링 관리자 도구. 주문량과 재고량을 JSON 데이터 소스에서 조회·확인할 수 있다.

## 프로젝트 개요

- **목적**: 저장된 데이터 상태를 콘솔에서 실시간으로 조회하는 관리자 도구
- **데이터 형식**: JSON
- **데이터 접근**: 커스텀 CRUD 라이브러리 사용 (별도 구현 불필요)
- **주요 조회 항목**: 주문량(orders), 재고량(inventory)

## 기술 스택

- Python >= 3.14
- pytest 9.0.3 (테스트)
- 패키지 관리: uv (`pyproject.toml`)

## 프로젝트 구조

```
datamonitor/
├── CLAUDE.md
├── main.py              # 진입점: 메인 루프 + render()
├── config.py            # 경로 설정 + sys.path 주입 (json_store 임포트 전 필수)
├── display.py           # 콘솔 출력 유틸 (clear, section, table, now)
├── views/
│   ├── orders.py        # OrderView: get_all / get_by_status / get_summary
│   └── inventory.py     # InventoryView: get_all
├── data/
│   ├── orders.json      # 주문 데이터 (key: 주문ID)
│   └── inventory.json   # 재고 데이터 (key: 시료ID)
├── pyproject.toml
└── uv.lock
```

## 데이터 스키마

**orders.json**
```json
{
  "ORD-001": { "status": "RESERVED", "sample": "SMP-A", "quantity": 5, "created_at": "2026-05-07" }
}
```

**inventory.json**
```json
{
  "SMP-A": { "quantity": 85 }
}
```

## 아키텍처 원칙

- 데이터 CRUD는 커스텀 라이브러리에 위임한다. 직접 JSON 파일을 열거나 파싱하는 코드를 작성하지 않는다.
- 모니터링 도구는 읽기(Read) 전용 뷰에 집중한다.
- 콘솔 출력은 가독성을 우선한다 (표 형식, 컬럼 정렬 등).

## 핵심 기능 요구사항

### 1. 주문량 조회

주문은 아래 4단계 상태로 관리된다. 각 상태별 목록을 독립적으로 조회할 수 있어야 한다.

| 상태 | 설명 |
|------|------|
| `RESERVED` | 예약 접수 완료, 아직 확정 전 |
| `CONFIRMED` | 주문 확정 |
| `PRODUCING` | 생산 진행 중 |
| `RELEASE` | 출고 완료 |

- 전체 주문 목록 조회 (모든 상태 포함)
- 특정 상태만 필터링하여 조회
- 상태별 건수 요약 (예: RESERVED: 5건, CONFIRMED: 3건 …)

### 2. 재고량 조회

- 시료(sample) 단위로 현재 재고 수량을 조회한다
- 전체 시료 목록과 각 시료의 현재 재고 수량을 표 형식으로 표시한다

### 3. 실시간 갱신

- 일정 주기로 데이터를 다시 읽어 콘솔 화면을 갱신한다

## 개발 명령어

```powershell
# 실행
uv run python main.py

# 테스트
uv run pytest
```
