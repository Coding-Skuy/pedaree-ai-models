# Modul pantry-resep — Kontrak Pawonee (pemilik) dan Pedaree (konsumen)

TownHall Pedaree: https://github.com/Coding-Skuy/Pedaree-TownHall

## Kedudukan

- **Pemilik:** Pawonee.
- **Konsumen:** Pedaree ai-models (memakai `recipe_id` sebagai fitur konteks).

## Aturan konsumen (berlaku untuk ai-models)

1. Daftar resep populer dari Pawonee dipakai sebagai bobot prioritas bahan.
2. Model tidak mengubah atau melatih ulang definisi resep.
3. Keluaran model: skor risiko kedaluwarsa per item dan urutan pakai yang
   disarankan, lengkap dengan rujukan `recipe_id` bila relevan.
