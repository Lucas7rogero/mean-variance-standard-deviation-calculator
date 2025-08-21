import numpy as np

def calculate(numbers):
    # confere se tem 9 numeros exatos na lista
    if len(numbers) != 9:
        raise ValueError("List must contain nine numbers.")

    # transformando a lista em uma matriz 3x3
    matrix = np.array(numbers).reshape(3, 3)

    # calculando as estatisticas que foram pedidas
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(), # media por coluna
            matrix.mean(axis=1).tolist(), # média por linha
            matrix.mean().tolist() # media total
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations
