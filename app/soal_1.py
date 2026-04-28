from InquirerPy import inquirer
from app.ui import console, print_banner, print_section, print_kv_table, print_back_hint
from app.validators import ValidatorFn, alpha_space, min_chars, has_digit

_FieldSchema = tuple[str, ValidatorFn, str]

_BIODATA_SCHEMA: list[_FieldSchema] = [
    (
        "Masukkan nama anggota perpustakaan",
        alpha_space(2),
        "Hanya huruf dan spasi, minimal 2 karakter",
    ),
    (
        "Masukkan alamat anggota perpustakaan",
        min_chars(3),
        "Alamat minimal 3 karakter",
    ),
    (
        "Masukkan tempat lahir anda",
        alpha_space(2),
        "Hanya huruf dan spasi, minimal 2 karakter",
    ),
    (
        "Masukkan tanggal lahir anda",
        has_digit(),
        "Harus mengandung angka, contoh: 1 Januari 2016",
    ),
]

_BUKU_SCHEMA: list[_FieldSchema] = [
    (
        "Masukkan nama judul buku pinjaman",
        min_chars(2),
        "Judul buku minimal 2 karakter",
    ),
    (
        "Masukkan nama pengarang buku",
        alpha_space(2),
        "Hanya huruf dan spasi, minimal 2 karakter",
    ),
    (
        "Masukkan nama penerbit buku",
        min_chars(2),
        "Nama penerbit minimal 2 karakter",
    ),
]


def _collect(schema: list[_FieldSchema], heading: str) -> list[str]:
    result: list[str] = []
    console.print(f"[header]{heading}[/]\n")
    for message, validate, invalid_message in schema:
        value: str = inquirer.text(
            message=message,
            validate=validate,
            invalid_message=invalid_message,
        ).execute()
        result.append(value.strip())
    return result


def run() -> None:
    try:
        print_banner()
        print_section("Soal 1A · Form Peminjaman Buku Perpustakaan")
        print_back_hint()

        biodata = _collect(_BIODATA_SCHEMA, "── Data Anggota Perpustakaan")
        console.print()
        buku = _collect(_BUKU_SCHEMA, "── Data Buku Pinjaman")

        console.print()
        console.rule(style="dim cyan")
        console.print()

        print_kv_table(
            [
                ("Biodata Anggota Perpustakaan", str(biodata)),
                ("Buku yang dipinjam", str(buku)),
            ]
        )
        console.print()

    except KeyboardInterrupt:
        console.print("\n\n  [muted]↩  Kembali ke menu utama...[/]\n")
