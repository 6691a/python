"""
keyword: Contextlib
"""
import time


class Timer():
    def __init__(self, msg: str) -> None:
        self._msg = msg
    
    def __enter__(self) -> float:
        self._start = time.monotonic()
        return self._start
    
    def __exit__(self, exc_type, exc_value, exc_traceback) -> bool:
        if exc_type:
            print(f"exception: {exc_value} / {exc_traceback}")
            return False
        
        print(f"{self._msg} : {time.monotonic() - self._start}")
        return True

with Timer("Time Start") as t:
    print(t, "1")
    raise Exception("ERROR")