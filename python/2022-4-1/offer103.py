class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount == 0:
            return 0
        coins=list(dict.fromkeys(coins))
        table = [None] * (amount + 1)
        for i in range(0, amount + 1):
            if i == 0 or table[i] != None:
                for j in coins:
                    if i + j > amount:
                        continue
                    if table[i + j] == None:
                        if table[i] == None:
                            table[i + j] = [j]
                        else:
                            table[i + j] = table[i].copy()
                            table[i + j].append(j)
                    else:
                        if len(table[i]) + 1 >= len(table[i + j]):
                            continue
                        else:
                            table[i + j] = table[i].copy()
                            table[i + j].append(j)
        if table[amount] == None:
            return -1
        return len(table[amount])


s = Solution()
print(s.coinChange([281, 20, 251, 251], 7323))
