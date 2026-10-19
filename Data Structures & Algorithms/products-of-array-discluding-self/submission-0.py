import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        final = []
        for i, n in enumerate(nums):
            print("i: ", i)
            print("n: ", n)
            print("___________")
            if i == 0:                              # start
                print("nums[0+1:] >>", nums[1:])
                print("___________")
                final.append(math.prod(nums[1:]))
            elif i == len(nums) - 1:                # end
                print("nums[:i] >>", nums[:i])
                print("___________")
                final.append(math.prod(nums[:i]))
            else:                                   # middle
                print("nums[" + str(i) + "] >>", nums[:i])
                print("nums[" + str(i+1) + "] >>", nums[i+1:])
                print("___________")
                final.append(math.prod(nums[:i]) * math.prod(nums[i+1:]))
        
        return final
        