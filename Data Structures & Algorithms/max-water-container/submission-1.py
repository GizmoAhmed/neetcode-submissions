class Solution:
    def maxArea(self, heights: List[int]) -> int:
        r = 0
        i = 0 
        j = len(heights) - 1
        area = (j - i) * min(heights[i], heights[j])
        while i < j:
            area = (j - i) * min(heights[i], heights[j])
            r = max(r, area)
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return r

        