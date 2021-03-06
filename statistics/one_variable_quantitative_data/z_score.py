"""
Algorithm
input = []
1. Calculate mean
    mean = fsum(input) / len(input)
2. Calculate standard deviation
    variance = [(x - mean) ** 2 for x in input] / len(input)
    std = math.sqrt(variance)
3. Calculate z-score (standard score)
    z-scores = [ (x - mean) / std for x in input]
"""
from math import fsum, sqrt
from typing import Iterable
from pprint import pprint
import pandas as pd
from scipy import stats


def mean(nums: Iterable):
    return fsum(nums) / len(nums)


def std(nums: Iterable):
    _mean = mean(nums)
    variance = sum([(x - _mean) ** 2 for x in nums]) / len(nums)
    return sqrt(variance)


def zScore(nums: Iterable):
    _std = std(nums)
    _mean = mean(nums)
    return [(x - _mean) / _std for x in nums]

def zScore_using_pandas(nums: Iterable):
    df = pd.DataFrame({'returns': nums})
    _std = df.std(ddof=0).loc['returns']
    _mean = df.mean().loc['returns']
    df['z_scores'] =  (df['returns'] - _mean) / _std
    return list(df['z_scores'])

def zScore_using_scipy(nums: Iterable):
    return stats.zscore(nums, ddof=0)

if __name__ == '__main__':
    pprint(zScore([4, 5, 6, 6, 6, 7, 8, 12, 13, 13, 14, 18]))
    print('#' * 80)
    pprint(zScore_using_pandas([4, 5, 6, 6, 6, 7, 8, 12, 13, 13, 14, 18]))
    print('#' * 80)
    pprint(zScore_using_scipy([4, 5, 6, 6, 6, 7, 8, 12, 13, 13, 14, 18]))
