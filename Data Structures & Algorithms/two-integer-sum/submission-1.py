class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        # if size to small, it must be those elements
        if size == 2:
            return [0,1]

        sum_dict = {}

        i = 0
        for curr in nums:
            pair_val = target - curr
            if pair_val in sum_dict: # if pair val is an existing key and key is not itself
                match = sum_dict[pair_val]
                # print(sum_dict)
                # print("MATCH <<<" + str(match) + ">>>")
                return [match[1], i]

            elif pair_val not in sum_dict:
                sum_dict[curr] = (pair_val, i)
            
            i += 1

        print(sum_dict)
        print("<<< DUPE KEY FOUND >>>")
        
        
        