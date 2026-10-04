"""Inferensi risiko kedaluwarsa memakai model ONNX ringan."""
from pathlib import Path

import numpy as np
import onnxruntime as ort
from pydantic import BaseModel


class FiturItem(BaseModel):
    sisa_hari: float
    laju_pakai_harian: float
    bobot_resep: float = 0.0


MODEL = Path(__file__).resolve().parent.parent / "models" / "kedaluwarsa-v1.onnx"


def skor_risiko(fitur: FiturItem) -> float:
    if not MODEL.exists():
        # Aturan cadangan bila artefak belum dibangun: heuristik murni.
        if fitur.sisa_hari < 0:
            return 1.0
        if fitur.sisa_hari <= 3:
            return 0.85
        if fitur.sisa_hari <= 7:
            return 0.6
        return 0.2
    sesi = ort.InferenceSession(str(MODEL))
    masukan = np.array(
        [[fitur.sisa_hari, fitur.laju_pakai_harian, fitur.bobot_resep]],
        dtype=np.float32,
    )
    keluar = sesi.run(None, {sesi.get_inputs()[0].name: masukan})
    return float(keluar[1][0][1])


if __name__ == "__main__":
    contoh = FiturItem(sisa_hari=2, laju_pakai_harian=1.0, bobot_resep=0.9)
    print(f"skor risiko: {skor_risiko(contoh):.2f}")
