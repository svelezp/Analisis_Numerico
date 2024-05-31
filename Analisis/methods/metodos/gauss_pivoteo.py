import numpy as np


def gauss_partial_pivot(a, b):
    ab = to_aug(a, b)
    assert a.shape[0] == a.shape[1]
    res = []
    res.append(np.copy(ab).tolist())
    size = a.shape[0]

    # Stages
    for k in range(0, size - 1):
        partial_pivot(ab, k)
        # Compute multiplier for row in stage.
        for i in range(k + 1, size):
            multiplier = ab[i][k] / ab[k][k]
            for j in range(k, size + 1):
                ab[i][j] = ab[i][j] - (multiplier * ab[k][j])
        res.append(np.copy(ab).tolist())
    x = regressive_substitution(ab)
    return res, x


def to_aug(a, b):
    return np.column_stack((a, b))


def regressive_substitution(ab, labels=None):
    size = ab.shape[0]
    assert ab.shape[1] == size + 1

    solutions = np.zeros(size, dtype=np.float64)
    solutions[size - 1] = ab[size - 1][size] / ab[size - 1][size - 1]

    # Loop backwards
    for i in range(size - 2, -1, -1):
        accum = 0
        for p in range(i + 1, size):
            accum += ab[i][p] * solutions[p]
        solutions[i] = (ab[i][size] - accum) / ab[i][i]

    # Update the labels and assign its values
    labeled_xs = np.zeros(size)
    if labels is not None:
        for i, v in enumerate(labels):
            labeled_xs[labels[i]] = solutions[i]
        solutions = labeled_xs

    return solutions


def partial_pivot(ab, k):
    largest = abs(ab[k][k])
    largest_row = k
    size = ab.shape[0]

    for r in range(k + 1, size):
        current = abs(ab[r][k])
        if current > largest:
            largest = current
            largest_row = r
    if largest == 0:
        raise Exception("Equation system does not have unique solution.")
    else:
        if largest_row != k:
            ab[[k, largest_row]] = ab[[largest_row, k]]
