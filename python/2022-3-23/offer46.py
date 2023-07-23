class Solution(object):
    def translateNum(self, num):
        """
        :type num: int
        :rtype: int
        """
        alphabet = [i for i in range(26)]
        s = str(num)
        n = len(s)
        table = [1, 1]
        for i in range(1, n):
            '''
            IMPORTANT: if we have table[i-1], then if s[i-1]s[i] cannot be translated,
            then table[i] = table[i-1]!!!! 
            eg. 18580: now we have table[2]: ways to translate 185 
            then let's see 185[8], 58 cannot be translated, so the number of ways to
            translate 1858 is same as the number of ways to translate 185!!!!!!
            
            else if 181[4] then ways to translate 1814 is [181] + [18] since we can have 2 ways to 
            translate: 4 or 14.
            '''
            if int(s[i - 1:i + 1]) in alphabet and int(s[i - 1]) != 0:
                table.append(table[i] + table[i - 1])
            else:
                table.append(table[i])
        return table[len(table) - 1]

    '''
    1 8 5 8 0 ok
    18 5 8 0 ok
    1 85 8 0 
    1 8 58 0 
    1 8 5 80
    
    18 58 0
    1 85 80 
    18 5 80
    '''


s = Solution()
print(s.translateNum(220))
