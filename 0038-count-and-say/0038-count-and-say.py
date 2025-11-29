class Solution:
    def countAndSay(self, n):
        result = "1"
        
        for _ in range(1, n):
            result = self.encode(result)
        
        return result
    
    def encode(self, s):
        res = ""
        i = 0
        
        while i < len(s):
            count = 1
            
           
            while i + 1 < len(s) and s[i] == s[i + 1]:
                count += 1
                i += 1
            
            
            res += str(count) + s[i]
            i += 1
        
        return res
