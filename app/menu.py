from InquirerPy import inquirer
from InquirerPy.base.control import Choice
from app.ui import console, print_banner, print_section, pause
from app import soal_1, soal_2, soal_3

_CHOICES: list[Choice] = [
    Choice(value="soal1", name="  1.  Form Peminjaman Buku Perpustakaan"),
    Choice(value="soal2", name="  2.  Penghapusan Elemen List"),
    Choice(value="soal3", name="  3.  Fungsi Len, Max dan Min pada Tuple"),
    Choice(value="exit",  name="  ✕   Keluar"),
]

_DISPATCH: dict[str, object] = {
    "soal1": soal_1,
    "soal2": soal_2,
    "soal3": soal_3,
}


def run_menu() -> None:
    while True:
        try:
            print("\x1Bc")
            print_banner()
            print_section("Menu Utama · Soal A (NIM Ganjil)")

            choice: str = inquirer.select(
                message="Pilih soal yang ingin dijalankan:",
                choices=_CHOICES,
                vi_mode=False,
            ).execute()

        except KeyboardInterrupt:
            print("\x1Bc")
            console.print("\n  [success]Terima kasih! Program selesai.[/]\n")
            break

        if choice == "exit":
            print("\x1Bc")
            console.print("\n  [success]Terima kasih! Program selesai.[/]\n")
            break

        print("\x1Bc")

        module = _DISPATCH.get(choice)
        if module is not None:
            getattr(module, "run")()

        pause()
