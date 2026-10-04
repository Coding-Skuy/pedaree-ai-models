# Arsitektur pedaree-ai-models

TownHall: https://github.com/Coding-Skuy/Pedaree-TownHall

## Lapisan

1. Fitur: sisa hari kedaluwarsa, laju pakai dari mutasi, konteks `recipe_id`.
2. Model: regresi logistik scikit-learn yang diekspor ke ONNX.
3. Inferensi: `src/inferensi.py` memuat `models/kedaluwarsa-v1.onnx` lewat
   onnxruntime dan mengembalikan skor risiko 0 sampai 1.

## Alur utama

Backend mengirim fitur item -> model menghitung risiko -> backend mengurutkan
saran pemakaian dan menampilkan resep Pawonee yang memakai bahan berisiko.

## Keputusan

- Model kecil dan dapat dijelaskan; berjalan di perangkat tanpa server GPU.
- Ambang risiko baku: di atas 0,7 berarti "segera pakai".
