from app.ui import console, print_banner, print_section, print_kv_table, print_back_hint

_A: tuple[str, ...] = (
    "Program", "Studi", "Teknik", "Informatika", "Fakultas", "Saintek", "Unisnu"
)

_B: tuple[int, ...] = (
    10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 300, 400, 500
)


def run() -> None:
    try:
        print_banner()
        print_section("Soal 3A · Fungsi Len, Max dan Min pada Tuple")
        print_back_hint()

        console.print(f"  [muted]A[/] [secondary]=[/] [primary]{_A}[/]")
        console.print(f"  [muted]B[/] [secondary]=[/] [primary]{_B}[/]")
        console.print()

        print_kv_table(
            [
                ("Menentukan nilai len dari elemen A adalah", str(len(_A))),
                ("Menentukan nilai len dari elemen B adalah", str(len(_B))),
                ("", ""),
                ("Menentukan nilai maximum atau terbesar dari elemen A adalah", str(max(_A))),
                ("Menentukan nilai minimum atau terkecil dari elemen A adalah", str(min(_A))),
                ("", ""),
                ("Menentukan nilai maximum atau terbesar dari elemen B adalah", str(max(_B))),
                ("Menentukan nilai minimum atau terkecil dari elemen B adalah", str(min(_B))),
            ]
        )

        console.print()

    except KeyboardInterrupt:
        console.print("\n\n  [muted]↩  Kembali ke menu utama...[/]\n")
