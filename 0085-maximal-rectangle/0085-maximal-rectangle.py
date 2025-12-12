class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * cols
        max_area = 0

        for r in range(rows):
           
            for c in range(cols):
                if matrix[r][c] == '1':
                    heights[c] += 1
                else:
                    heights[c] = 0

          
            max_area = max(max_area, self._largestRectangleArea(heights))

        return max_area

    def _largestRectangleArea(self, heights):
        """Largest rectangle in histogram (standard monotonic stack)."""
        
        h = heights + [0]
        stack = [-1]  
        max_area = 0

        for i, height in enumerate(h):
           
            while stack and stack[-1] != -1 and h[stack[-1]] > height:
                height_idx = stack.pop()
                height_val = h[height_idx]
                width = i - stack[-1] - 1
                max_area = max(max_area, height_val * width)
            stack.append(i)

        return max_area
