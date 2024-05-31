import numpy as np


def gauss_simple(a, b):
    ab = to_aug(a, b)
    res = []
    res.append(np.copy(ab).tolist())
    assert a.shape[0] == a.shape[1]

    size = a.shape[0]

    # Stages

    for i in range(0, size - 1):
        # Compute multiplier for row in stage.
        for j in range(i + 1, size):
            multiplier = ab[j][i] / ab[i][i]
            for k in range(i, size + 1):
                ab[j][k] = ab[j][k] - (multiplier * ab[i][k])
        res.append(np.copy(ab).tolist())

    return res


def to_aug(a, b):
    return np.column_stack((a, b))
