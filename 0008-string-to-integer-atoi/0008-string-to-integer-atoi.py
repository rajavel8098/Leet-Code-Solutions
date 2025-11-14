class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """

        INT_MIN = -2**31        
        INT_MAX = 2**31 - 1     

        i = 0
        n = len(s)

       
        while i < n and s[i] == ' ':
            i += 1

        
        if i == n:
            return 0

       
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1

       
        num = 0
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')

            
            if num > (INT_MAX // 10) or (num == INT_MAX // 10 and digit > INT_MAX % 10):
                return INT_MAX if sign == 1 else INT_MIN

            num = num * 10 + digit
            i += 1

        return num * sign
