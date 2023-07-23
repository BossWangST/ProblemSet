from functools import *
from typing import *
from itertools import *
from math import *
from collections import *
from itertools import *
from heapq import *
from bisect import *
from multiprocessing import *

from threading import *


class ZeroEvenOdd:
    def __init__(self, n):
        self.n = n
        self.cur = 1
        self.tick = True
        self.n0 = Lock()
        self.n1 = Lock()
        self.n2 = Lock()
        self.n1.acquire()
        self.n2.acquire()

    # printNumber(x) outputs "x", where x is an integer.
    def zero(self, printNumber: 'Callable[[int], None]') -> None:
        print('Now is Zero')
        for i in range(self.n):
            self.n0.acquire()
            printNumber(0)
            if self.tick:
                self.n1.release()
            else:
                self.n2.release()
            self.tick = not self.tick

    def even(self, printNumber: 'Callable[[int], None]') -> None:
        print('Now is Even')
        while self.cur <= self.n:
            self.n2.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.n0.release()

    def odd(self, printNumber: 'Callable[[int], None]') -> None:
        print('Now is Odd')
        while self.cur <= self.n:
            self.n1.acquire()
            printNumber(self.cur)
            self.cur += 1
            self.n0.release()

