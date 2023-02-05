import bentoml
from bentoml.io import NumpyNdarray
import numpy as np

runner = bentoml.sklearn.get('lr_classifier:latest').to_runner()

svc = bentoml.Service('classifier', runners=[runner])

@svc.api(input=NumpyNdarray(shape=(-1,4), enforce_shape=True), output=NumpyNdarray())
def classify(input: np.ndarray)->np.ndarray:
    return runner.run(input)