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


if __name__ == '__main__':
    pprint(zScore([4, 5, 6, 6, 6, 7, 8, 12, 13, 13, 14, 18]))
