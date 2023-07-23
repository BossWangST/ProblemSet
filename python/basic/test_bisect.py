import collections

import bisect

a = [5, 5, 7, 7, 8, 8, 8, 8, 9]


def check(limit: int) -> bool:
    if limit >= 8:
        return True
    else:
        return False


print(bisect.bisect_left(a, True, key=check))
