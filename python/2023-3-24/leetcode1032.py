from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *


class StreamChecker:

    def __init__(self, words: List[str]):
        self.d = defaultdict(set)
        for word in words:
            self.d[len(word)].add(word)
        self.cur = ""

    def query(self, letter: str) -> bool:
        self.cur += letter
        for key, val in self.d.items():
            word = self.cur[len(self.cur) - key:]
            if word in val:
                return True
        return False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
