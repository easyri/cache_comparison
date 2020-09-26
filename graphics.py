from quick import get_stats
import random
import pickle
from new_cacheout import lru_memoize, lifo_memoize, fifo_memoize, lfu_memoize, mru_memoize, rr_memoize


def get_arr(n, max):
    nums = []
    for i in range(n):
        nums.append(random.randrange(max))
    return nums


def get_all_stats(cached_algo, nums, max_size,  min_size=0, step=5):
    timings = []
    hits = []
    misses = []
    size = []
    for i in range(min_size, max_size, step):
        cached = memo(cached_algo, i)
        stats = get_stats(cached, nums)
        timings.append(stats['time'])
        hits.append(stats['hit'])
        misses.append(stats['miss'])
        size.append(i)
    return {'size': size, 'timings': timings, 'hits': hits, 'misses': misses}


def memo(memo, max):
    @memo(maxsize=max)
    def quicksort_m(nums):
        if len(nums) <= 1:
            return nums
        q = random.choice(nums)
        l_nums = [n for n in nums if n < q]
        e_nums = [q] * nums.count(q)
        b_nums = [n for n in nums if n > q]
        result = quicksort_m(l_nums) + e_nums + quicksort_m(b_nums)
        return result
    return quicksort_m


def more_stats(nums, max, min=0, step=1):

    stats_dict = dict()
    for algo in lru_memoize, lifo_memoize, fifo_memoize, lfu_memoize, mru_memoize, rr_memoize:
        name = str(algo).split()[1]
        stats_dict[name] = get_all_stats(algo, nums, max, min, step)
    return stats_dict


if __name__ == "__main__":
    nums = get_arr(100, 40)
    # print(get_all_stats(rr_memoize, nums, 10, 0, 1))
    stats = more_stats(nums, 10, 0, 1)
    a_file = open("data.pkl", "wb")
    pickle.dump(stats, a_file)
    a_file.close()

    a_file = open("data.pkl", "rb")
    stats2 = pickle.load(a_file)
    print(stats2)



