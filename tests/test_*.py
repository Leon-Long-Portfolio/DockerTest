import pytest
import logging
from matrix_multi import matrix_multiply

logging.basicConfig(filename='test_matrix.log', level=logging.DEBUG)

def test_correct_multiplication():
    logging.info("Testing correct multiplication.")
    # Test Case 1: Correct Multiplication
    A = [[1, 2, 3],
         [4, 5, 6]]

    B = [[7, 8],
         [9, 10],
         [11, 12]]

    result = matrix_multiply(A, B)

    assert result == [[58, 64],
                      [139, 154]]

def test_matrix_multiply_incorrect_dimensions():
    logging.info("Testing incorrect dimensions.")
    # Test case 2: Incorrect dimensions
    C = [[1, 2, 3],
         [4, 5, 6]]
    D = [[1, 2],
         [3, 4]]

    with pytest.raises(ValueError) as e:
        matrix_multiply(C, D)
    assert str(e.value) == "ERROR: Matrix Dimensions."

def test_matrix_multiply_empty_matrices():
    logging.info("Testing empty matrices.")
    # Test Case 3: Handling empty matrices
    E = []
    F = []
    
    assert matrix_multiply(E, F) == []

def test_matrix_multiply_identity_matrix():
    logging.info("Testing multiplication by identity matrix.")
    # Test Case 4: Multiplication by an identity matrix
    G = [[1, 0],
          [0, 1]]
    
    H = [[2, 3],
          [4, 5]]
    
    assert matrix_multiply(G, H) == H
