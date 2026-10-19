class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        r = []
        nums.sort()
        i = 0

        while i < len(nums):
            if i > 0 and nums[i] == nums[i - 1]:
                i += 1
                continue

            j = i + 1
            k = len(nums) - 1
            target = -nums[i]

            while j < k:
                front = nums[j]
                back = nums[k]
                if front + back == target:
                    r.append([nums[i], front, back])

                    while j < k and nums[j] == nums[j + 1]:
                        j += 1
                    while j < k and nums[k] == nums[k - 1]:
                        k -= 1

                    j += 1
                    k -= 1
                elif front + back < target:
                    j += 1
                else:
                    k -= 1

            i += 1

        return r
