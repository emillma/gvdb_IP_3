import numpy as np


def ostu(img: np.ndarray) -> float:
    hist = np.histogram(img)
    hist_norm = hist / img.size()
    P1 = np.cumsum(hist_norm)

    mean = np.mean(img)
    globals().update(locals())
