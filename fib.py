import timeit

from functools import lru_cache
from new_cacheout import lru_memoize, lifo_memoize, fifo_memoize
from new_cacheout import Cache


@lifo_memoize(maxsize=3)
def fib_lifo(n):
    if n <= 2:
        return 1
    else:
        return fib_lifo(n-1) + fib_lifo(n-2)

@fifo_memoize(maxsize=3)
def fib_fifo(n):
    if n <= 2:
        return 1
    else:
        return fib_fifo(n-1) + fib_fifo(n-2)

@lru_memoize(maxsize=3)
def fib_lru(n):
    if n <= 2:
        return 1
    else:
        return fib_lru(n-1) + fib_lru(n-2)


@lru_cache(maxsize=3)
def fib_lru_func(n):
    if n <= 2:
        return 1
    else:
        return fib_lru_func(n-1) + fib_lru_func(n-2)


if __name__ == "__main__":
    cachet = Cache()
    print(cachet.get(key=1, default=3))
    n = 100

    print(timeit.timeit(lambda: fib_lru(n), number=100))
    print(fib_lru.cache.hit, fib_lru.cache.miss, fib_lru.cache.all, sep=' ')

    print(timeit.timeit(lambda: fib_lru_func(n), number=100))
    print(fib_lru_func.cache_info())

    print(timeit.timeit(lambda: fib_fifo(n), number=100))
    print(fib_fifo.cache.hit, fib_fifo.cache.miss, fib_fifo.cache.all, sep=' ')

    # print(timeit.timeit(lambda: fib_lifo(n), number=100))