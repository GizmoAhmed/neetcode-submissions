class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        memo = {}
        for n in nums:
            if (n not in memo):
                memo[n] = 1
            else:
                return True
        return False
        