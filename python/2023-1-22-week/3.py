from typing import List
import collections
import bisect
import functools
import math
import itertools
import heapq


class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort(key=lambda x: -(x[:][k]))
        return score
