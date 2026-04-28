[![Workflow Status](https://img.shields.io/github/actions/workflow/status/decryptable/data-structure/build.yml?style=for-the-badge&logo=gitforwindows&cacheSeconds=0)](https://github.com/decryptable/data-structure/actions/workflows/build.yml)
[![Latest Release](https://img.shields.io/github/downloads/decryptable/data-structure/latest/data-structure.pyz?displayAssetName=true&sort=semver&style=for-the-badge&logo=abdownloadmanager&cacheSeconds=0)](https://github.com/decryptable/data-structure/releases/latest/download/data-structure.pyz)

# Struktur Data — UTS Genap 2025/2026

|                 |                                 |
| --------------- | ------------------------------- |
| **Nama**        | Ichsan Hafizd Al-Fajry          |
| **NIM**         | 251240001657                    |
| **Mata Kuliah** | Struktur Data · Kelas 2TIFA     |
| **Dosen**       | R. Hadapiningradja K, M.Kom     |
| **Soal**        | A (NIM Ganjil — digit akhir: 7) |

---

## Daftar Soal

| No  | Judul                              | Konsep                                     |
| --- | ---------------------------------- | ------------------------------------------ |
| 1A  | Form Peminjaman Buku Perpustakaan  | `list`, `input`, `append`                  |
| 2A  | Penghapusan Elemen List            | `list`, `while`, `elif`, `break`, `remove` |
| 3A  | Fungsi Len, Max dan Min pada Tuple | `tuple`, `len`, `max`, `min`               |

---

## Struktur Project

```
data-structure/
├── .github/
│   └── workflows/
│       └── build.yml        # CI/CD → Nuitka → GitHub Releases
├── app/
│   ├── __init__.py
│   ├── ui.py                # Shared console, theme, helpers
│   ├── menu.py              # Interactive main menu
│   ├── soal_1.py            # Form Peminjaman Buku
│   ├── soal_2.py            # Hapus Elemen List
│   └── soal_3.py            # Tuple Len/Max/Min
├── main.py                  # Entry point (click)
├── launcher.ps1             # PowerShell launcher
├── start.bat                # Double-click → buka PowerShell
├── pyproject.toml
├── requirements.txt
└── README.md
```

---

## Menjalankan dari Source

```powershell
pip install -r requirements.txt
pip install -e .
python main.py
```

## Menjalankan Executable (Windows)

Buka CMD lalu jalankan kode berikut:

```cmd
powershell -NoProfile -Command "$u='https://github.com/decryptable/data-structure/releases/latest/download/data-structure.pyz'; $t=\"$env:TEMP\data-structure.pyz\"; Invoke-WebRequest -Uri $u -OutFile $t -ErrorAction SilentlyContinue; python $t; Remove-Item -Path $t -ErrorAction SilentlyContinue;"
```

Atau double-click **`start.bat`**.
