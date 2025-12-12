class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3:
            return False

        
        dp = [False] * (n2 + 1)
        dp[0] = True

       
        for j in range(1, n2 + 1):
            dp[j] = dp[j - 1] and (s2[j - 1] == s3[j - 1])

        for i in range(1, n1 + 1):
           
            dp[0] = dp[0] and (s1[i - 1] == s3[i - 1])
            for j in range(1, n2 + 1):
               
                take_from_s1 = dp[j] and (s1[i - 1] == s3[i + j - 1])
                take_from_s2 = dp[j - 1] and (s2[j - 1] == s3[i + j - 1])
                dp[j] = take_from_s1 or take_from_s2

        return dp[n2]
