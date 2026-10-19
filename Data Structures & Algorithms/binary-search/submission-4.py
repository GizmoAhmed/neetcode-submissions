class Solution:
    def search(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        p = None

        while True:
            curr = nums[mid]
            if curr == target:
                return mid

            if curr > target:
                mid -= 1
                
                if p == None: # first spass
                    p = False;
                elif p == True: # it went back up again, meaning it passed what wasn't there
                    return -1

                
            elif curr < target:
                mid += 1

                if p == None: # first spass
                    p = True;
                if p == False: # it went back up again, meaning it passed what wasn't there
                    return -1
                
            if mid > len(nums) - 1 or mid == -1:
                return -1

        