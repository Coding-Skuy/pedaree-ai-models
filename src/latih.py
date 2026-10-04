"""Latih model risiko kedaluwarsa dan ekspor ke ONNX."""
import numpy as np
from sklearn.linear_model import LogisticRegression
from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType

rng = np.random.default_rng(42)
X = rng.normal(size=(200, 3)).astype(np.float32)
y = (X[:, 0] < 0).astype(int)

model = LogisticRegression().fit(X, y)
onnx_model = convert_sklearn(
    model, initial_types=[("masukan", FloatTensorType([None, 3]))]
)
with open("models/kedaluwarsa-v1.onnx", "wb") as f:
    f.write(onnx_model.SerializeToString())
print("model tersimpan di models/kedaluwarsa-v1.onnx")
