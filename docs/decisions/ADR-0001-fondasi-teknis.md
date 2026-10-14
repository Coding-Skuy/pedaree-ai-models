# ADR-0001 — Fondasi teknis pedaree-ai-models

Status: Diterima | Tanggal: 2026-10-14

## Konteks

Pedaree memerlukan prioritas pemakaian bahan agar waste turun (<1.500 g / Rp50.000 per rumah tangga per bulan; ≥50% batch SEGERA dipakai). Sumber kebenaran: Pedaree-TownHall `platform/versions/v1.0.0` (https://github.com/Coding-Skuy/Pedaree-TownHall/tree/main/platform/versions/v1.0.0), beku 2026-10-07; lintas divisi: [KONTEKS-LINTAS-DIVISI.md](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/KONTEKS-LINTAS-DIVISI.md). Tiket fondasi: PDR-AI-001 (issue #1).

## Keputusan

1. Python untuk training dan evaluasi; serving selalu lewat API Rust, tidak dari repo ini.
2. Wajib: model card, metrik evaluasi, dan versi model pada tiap rilis; artefak ONNX.
3. Aturan deterministik FEFO + ambang SOP kedaluwarsa menjadi baseline; model hanya boleh menambah, tidak menggantikan, aturan terkunci.
4. `recipe_id` Pawonee dipakai sebagai fitur konteks; skema resep milik Pawonee dan tidak disalin.
5. DB per service: repo ini tidak menyentuh DB divisi lain; data latih berasal dari ekspor teranonimkan DB `pedaree`.

## Konsekuensi

- Setiap rilis model membutuhkan evaluasi dan pembaruan `eval/metrics.md`.
- Backend Rust memuat ONNX; perubahan format input/output model = bump versi + ADR.
- Model tidak boleh mengubah ambang SOP; keputusan ambang tetap milik TownHall.
