import os
from datetime import datetime


def clear() -> None:
    os.system("cls")


def section(title: str) -> str:
    bar = "=" * 56
    return f"{bar}\n  {title}\n{bar}"


def table(columns: list[tuple[str, int]], rows: list[list]) -> str:
    sep = "+" + "+".join("-" * (w + 2) for _, w in columns) + "+"
    head = "|" + "|".join(f" {h:<{w}} " for h, w in columns) + "|"
    lines = [sep, head, sep]
    for row in rows:
        lines.append("|" + "|".join(f" {str(v):<{w}} " for (_, w), v in zip(columns, row)) + "|")
    lines.append(sep)
    return "\n".join(lines)


def now() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
