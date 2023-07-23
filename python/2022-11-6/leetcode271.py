from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        res = ''
        for s in strs:
            res += s + '\n'
        return res

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        res = []
        cur_s = ''
        for c in s:
            if c != '\n':
                cur_s += c
            else:
                res.append(cur_s)
                cur_s = ''
        return res
