import numpy as np
from fastapi import APIRouter

router = APIRouter()


@router.get('')
def hello_world() -> dict:
    return {'msg': 'Hello, World!'}


@router.get("/multiply")
def multiply_matrices():
    matrix_a = np.random.randint(0, 10, (10, 10)).tolist()
    matrix_b = np.random.randint(0, 10, (10, 10)).tolist()
    product = np.dot(matrix_a, matrix_b).tolist()

    return {
        "matrix_a": matrix_a,
        "matrix_b": matrix_b,
        "product": product,
    }