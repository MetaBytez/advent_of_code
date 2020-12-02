from functools import wraps
from time import time


def timed(f):
    @wraps(f)
    def _wrapped(*args, **kwargs):
        start = time()
        to_return = f(*args, **kwargs)
        elapsed = time() - start
        print(f'Execution Time: {elapsed:0.4f}')
        return to_return
    return _wrapped
