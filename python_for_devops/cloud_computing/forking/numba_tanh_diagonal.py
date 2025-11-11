import numpy as np
from numba import jit
import time


@jit(nopython=True)
def go_fast(a):
    """Expects Numpy Array"""
    
    count = 0
    for i in range(a.shape[0]):
        count += np.tanh(a[i, i])
    return count

x = np.arange(100).reshape(10, 10)


def execution_time(func, *args):
    start = time.time()
    result = func(*args)
    end = time.time()
    print(f"Execution time for {func.__name__}:, {end - start:.8f} seconds")
    return result
    
execution_time(go_fast, x)
execution_time(go_fast.py_func, x)

