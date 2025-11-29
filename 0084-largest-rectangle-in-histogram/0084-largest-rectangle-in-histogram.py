class Solution(object):
    def largestRectangleArea(self, heights):
        stack = []  # stores (index, height)
        max_area = 0
        
        for i, h in enumerate(heights):
            start = i
           
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            
            stack.append((start, h))
        
       
        n = len(heights)
        while stack:
            index, height = stack.pop()
            max_area = max(max_area, height * (n - index))
        
        return max_area

        