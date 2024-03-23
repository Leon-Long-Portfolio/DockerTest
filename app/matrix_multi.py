import logging
import time
from memory_profiler import profile

logging.basicConfig(filename='matrix.log', level=logging.DEBUG)

# A * B = C
@profile
def matrix_multiply(A, B):
    logging.info("Matrix multiplication started.")
    
    start_time = time.time()
    
    # Handle empty matrices
    if not A or not A[0] or not B or not B[0]:
        logging.error("Empty matrices provided.")
        return []
        
    # A: x * y
    # B: y * z
    x = len(A)
    y = len(A[0])
    z = len(B[0])

    # Check dimensions
    if len(B) != y:
        logging.error("Matrix dimension mismatch.")
        raise ValueError("ERROR: Matrix Dimensions.")

    # Initialize C
    C = [[0] * z for _ in range(x)]

    # Matrix Multiplication
    for i in range(x):
        for j in range(z):
            for k in range(y):
                C[i][j] += A[i][k] * B[k][j]
              
    # Return result
    logging.info(f"Matrix multiplication completed in {time.time() - start_time} seconds.")
    return C
