import numpy as np


def normalise(x):
    """Normalise un vecteur de valeurs à une moyenne de 0 et un écart-type de 1."""
    return (x - np.mean(x)) / np.std(x)


if __name__ == "__main__":
    vec = [2, 4, 6, 8, 10]
    vec_norm = normalise(vec)
    print(np.mean(vec), np.var(vec), np.mean(vec_norm), np.var(vec_norm))
