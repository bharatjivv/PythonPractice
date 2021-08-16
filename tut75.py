import time
from functools import lru_cache

@lru_cache(maxsize=3)

def some_work(n):
    # Some task taknig n seconds
    time.sleep(n)
    return n

if __name__ == '__main__':
    print("Now running some work")
    some_work(3)
    print("Done... Calling Again")
    some_work(3)
    print("Called Again")