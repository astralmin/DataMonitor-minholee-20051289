import re
from display import section, table, now


def test_section_contains_title():
    assert "테스트 섹션" in section("테스트 섹션")


def test_section_separator_lines_match():
    lines = section("title").splitlines()
    assert lines[0] == lines[2]
    assert "=" in lines[0]


def test_table_contains_headers():
    result = table([("주문ID", 10), ("상태", 12)], [])
    assert "주문ID" in result
    assert "상태" in result


def test_table_contains_data_row():
    result = table([("ID", 8), ("값", 10)], [["ORD-001", "RESERVED"]])
    assert "ORD-001" in result
    assert "RESERVED" in result


def test_table_multiple_rows():
    result = table([("ID", 8), ("수량", 6)], [["SMP-A", "10"], ["SMP-B", "20"]])
    assert "SMP-A" in result
    assert "SMP-B" in result


def test_table_empty_rows_keeps_structure():
    result = table([("ID", 8)], [])
    assert "ID" in result
    assert "+" in result


def test_now_format():
    assert re.match(r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", now())
