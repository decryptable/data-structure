from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme
from rich.align import Align
from rich import box

_THEME = Theme(
    {
        "primary": "bold cyan",
        "secondary": "bold yellow",
        "success": "bold green",
        "error": "bold red",
        "muted": "dim white",
        "header": "bold white",
        "hint": "dim italic cyan",
    }
)

console: Console = Console(theme=_THEME, highlight=False)

_TITLE = "Struktur Data — UTS Genap 2025/2026 · UNISNU Jepara"
_AUTHOR = "Ichsan Hafizd Al-Fajry · NIM 251240001657"


def print_banner() -> None:
    panel = Panel(
        Align.center(f"[header]{_TITLE}[/]\n[muted]{_AUTHOR}[/]"),
        border_style="cyan",
        box=box.DOUBLE,
        padding=(1, 4),
    )
    console.print(panel)
    console.print()


def print_section(title: str) -> None:
    console.rule(f"[secondary] {title} [/]", style="cyan")
    console.print()


def print_back_hint() -> None:
    console.print("[hint]  ↩  Tekan Ctrl+C kapan saja untuk kembali ke menu utama[/]\n")


def print_kv_table(items: list[tuple[str, str]]) -> None:
    non_empty_keys = [k for k, _ in items if k.strip()]
    if not non_empty_keys:
        return
    width = max(len(k) for k in non_empty_keys)
    for label, value in items:
        if not label.strip():
            console.print()
        else:
            console.print(
                f"  [muted]{label.ljust(width)}[/]"
                f" [secondary]:[/]"
                f" [primary]{value}[/]"
            )


def print_list_state(label: str, items: list[str]) -> None:
    console.print(
        f"  [muted]{label}[/] [secondary]:[/] [primary]{items}[/]"
    )


def pause() -> None:
    console.print()
    try:
        console.input("[muted]  Tekan Enter untuk kembali ke menu...[/]")
    except KeyboardInterrupt:
        pass
