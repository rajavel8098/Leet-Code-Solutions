class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        # Constants for 32-bit range
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        # Edge case: overflow (most negative number / -1)
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # 1. Determine sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # 2. Work with positive values
        dividend = abs(dividend)
        divisor = abs(divisor)
        
        quotient = 0
        
        # 3. Subtract divisor multiples using bit shifts
        while dividend >= divisor:
            temp = divisor
            multiple = 1
            
            # Increase temp until shifting further would exceed dividend
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            
            # Subtract the largest shifted divisor
            dividend -= temp
            quotient += multiple
        
        # 4. Apply sign
        quotient *= sign
        
        # 5. Final clamp to 32-bit range
        if quotient < INT_MIN:
            return INT_MIN
        if quotient > INT_MAX:
            return INT_MAX
        
        return quotient
