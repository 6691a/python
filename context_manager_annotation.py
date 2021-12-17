"""
with 구문 이해
contextlib 데코레이터 사용
"""

import contextlib
import time

@contextlib.contextmanager
def timer():

    start = time.monotonic()
    try:
        # __enter__
        yield start
    except BaseException as e:
        print(e)
        raise
    else:

        # __exit__
        print(f"Time: {time.monotonic() - start}")

with timer() as t:
    print(t)
    for i in range(1000000):
        pass
    raise ValueError("Error")