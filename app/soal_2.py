from InquirerPy import inquirer
from app.ui import console, print_banner, print_section, print_list_state, print_back_hint
from app.validators import not_empty

_INITIAL_MOTOR: list[str] = [
    "honda", "yamaha", "suzuki", "kawasaki", "bajaj", "jialing"
]


def run() -> None:
    try:
        print_banner()
        print_section("Soal 2A · Penghapusan Elemen List")
        print_back_hint()

        motor: list[str] = list(_INITIAL_MOTOR)
        print_list_state("Daftar merk motor", motor)
        console.print()

        while True:
            objek: str = inquirer.text(
                message="Masukkan objek merk motor yang akan di hapus",
                validate=not_empty(),
                invalid_message="Input tidak boleh kosong",
            ).execute()

            objek = objek.strip()

            if objek.lower() == "stop":
                console.print("\n  [success]selesai[/]")
                break
            elif objek in motor:
                motor.remove(objek)
                print_list_state("Hasil List merk motor setelah di edit", motor)
            else:
                console.print(
                    f"  [error]✗  '{objek}' tidak ditemukan.[/]"
                    f" [muted]Pilihan valid: {motor} | stop[/]"
                )

            console.print()

    except KeyboardInterrupt:
        console.print("\n\n  [muted]↩  Kembali ke menu utama...[/]\n")
