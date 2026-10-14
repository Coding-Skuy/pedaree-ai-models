> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# ARSITEKTUR-AI-DEV — Stack terkunci dan batas context (pedaree-ai-models)

Mengacu: Pedaree-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pedaree-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07. Dokumen ini MELENGKAPI `versions/v1.0.0/docs/40-TECHSTACK.md` dan `versions/v1.0.0/docs/60-BLAST-RADIUS.md` (keduanya beku v1.0.0 dan tidak diedit; isinya hanya ringkasan satu paragraf). Tidak menduplikasi BRD/PRD/FRD/FSD/SRS.

Baris Pedaree townhall-roadmap §2: point of concern "FEFO; stockout <8%; waste <1.500 g/Rp50.000/bln"; batas context "13 satuan baku; konsumen modul `pantry-resep` milik Pawonee". Rujukan lintas divisi: KONTEKS §3.1, §6, §8, §9.

## 1. Matriks stack

| Komponen | Kondisi saat ini (tercatat dari manifes/README) | Target terkunci v1.0.0 |
|---|---|---|
| Python | 3.12.8 | 3.12.x (pin eksak saat kickoff) |
| ML | scikit-learn 1.6.1, numpy 2.0.2 | scikit-learn + numpy (eksak saat kickoff) |
| Ekspor/serving | onnx 1.18.0, onnxruntime 1.21.0, skl2onnx 1.18.0 | ONNX; serving hanya lewat API Rust |
| Validasi | pydantic 2.10.6 | pydantic 2.x |
| Uji | pytest 8.3.4 | pytest + evaluasi terhadap baseline |
| Dokumentasi model | belum ada | model card + `eval/metrics.md` + versi |

## 2. Catatan drift

- README memuat folder `models/` dan `tests/` yang belum ada di repo; dibuat lewat tiket PDR-AI-002..003.
- Belum ada model card dan metrik eval; dibuat lewat PDR-AI-003.

## 3. Boleh disentuh repo ini

- `src/` (latih, inferensi), `models/`, `eval/`, `tests/`, model card.
- Mengonsumsi ekspor teranonimkan dari DB `pedaree` untuk training.

## 4. Dilarang

- Melayani API publik atau menyentuh DB mana pun.
- Mengubah ambang SOP, FEFO, atau 13 satuan.
- Melatih ulang atau menyalin data resep Pawonee.
- Menyentuh DB divisi lain (DB per service; Titeny hanya read-only ke DB sumber).
- Membuat pesanan TitipO otomatis dari sinyal stok (hanya anjuran, relevansi 48 jam).
- Mengubah modul `:shared:pantry-resep` (milik Pawonee), daftar 13 satuan, ambang kedaluwarsa, atau audiens JWT tanpa PR TownHall + ADR.

## 5. Kontrak yang diproduksi

- Artefak ONNX + model card + `eval/metrics.md` + versi model.
- Kontrak masukan/keluaran model untuk API Rust.

## 6. Kontrak yang dikonsumsi

- Definisi FEFO/ambang dari `inventori/10` dan `notifikasi/10`.
- `recipe_id` Pawonee sebagai fitur konteks.

## 7. Dampak bila berubah

- Perubahan format model memecahkan pemuatan di backend Rust.
- Model yang lebih buruk dari baseline dapat menaikkan waste; rilis diblokir.

## Batasan

- Dokumen ini hanya mencatat stack dan batas; tidak mengubah manifes atau kode. Kondisi saat ini dicatat apa adanya.
- Versi dikunci eksak di manifes saat kickoff coding; perubahan dicatat lewat ADR baru.
- JWT audiens `pedaree`, DB logis `pedaree`, dan kepemilikan Pawonee atas `:shared:pantry-resep` tidak berubah oleh dokumen ini.
