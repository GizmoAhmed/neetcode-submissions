class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return min(nums[0], nums[1])

        m = len(nums) // 2
        l = 0
        r = len(nums) - 1
        
        while True:
            if nums[m] > nums[r]:   # search right
                l = m
            else:                   # search left
                r = m
            m = (l + r) // 2
            
            if l == r - 1:
                return min(nums[l], nums[r])
            
            


        