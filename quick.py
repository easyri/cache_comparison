import timeit
import random
from new_cacheout import lru_memoize, lifo_memoize, fifo_memoize, lfu_memoize, mru_memoize, rr_memoize


def quicksort(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort(l_nums) + e_nums + quicksort(b_nums)


def quicksort_memo(nums, cache=dict()):
    key = ','.join(map(str, nums))

    if len(nums) <= 1:
        return nums

    if key in cache:
        return cache[key]

    q = random.choice(nums)

    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]

    cache[key] = quicksort_memo(l_nums, cache) + e_nums + quicksort_memo(b_nums, cache)
    # print(cache)
    return cache[key]


@fifo_memoize(maxsize=3)
def quicksort_fifo(nums):
    #key = ','.join(map(str, nums))

    if len(nums) <= 1:
        return nums

    # if key in cache:
    #     return cache[key]

    q = random.choice(nums)

    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]

    result = quicksort_fifo(l_nums) + e_nums + quicksort_fifo(b_nums)
    # print(cache)
    return result


@lifo_memoize(maxsize=3)
def quicksort_lifo(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    result = quicksort_lifo(l_nums) + e_nums + quicksort_lifo(b_nums)
    return result

@lru_memoize(maxsize=3)
def quicksort_lru(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    result = quicksort_lru(l_nums) + e_nums + quicksort_lru(b_nums)
    return result

@lfu_memoize(maxsize=3)
def quicksort_lfu(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    result = quicksort_lfu(l_nums) + e_nums + quicksort_lfu(b_nums)
    return result

@mru_memoize(maxsize=3)
def quicksort_mru(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    result = quicksort_mru(l_nums) + e_nums + quicksort_mru(b_nums)
    return result

@rr_memoize(maxsize=3)
def quicksort_rr(nums):
    if len(nums) <= 1:
        return nums
    q = random.choice(nums)
    l_nums = [n for n in nums if n < q]
    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    result = quicksort_rr(l_nums) + e_nums + quicksort_rr(b_nums)
    return result




def get_stats(cached_func, arg):
    time = timeit.timeit(lambda: cached_func(arg), number=100)
    hit, miss = cached_func.cache.hit, cached_func.cache.miss
    return {'name': cached_func, 'time': time, 'hit': hit, 'miss': miss}


if __name__ == "__main__":
    nums = []
    for i in range(100):
        nums.append(random.randrange(40))

    print(nums)
    print(quicksort_memo(nums))
    print('pure quick', timeit.timeit(lambda: quicksort(nums), number=100), sep=': ')
    print('all cached', timeit.timeit(lambda: quicksort_memo(nums), number=100), sep=': ')
    # print(quicksort(nums) == quicksort_memo(nums))

    # print(get_stats(quicksort_fifo, nums))
    print(get_stats(quicksort_lifo, nums))
    print(get_stats(quicksort_lru, nums))
    print(get_stats(quicksort_lfu, nums))
    print(get_stats(quicksort_mru, nums))

    quicksort_rr = rr_memoize(maxsize=3)(quicksort_rr)
    print(get_stats(quicksort_rr, nums))
