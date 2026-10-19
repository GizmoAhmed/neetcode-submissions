class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hsh = {}
        for n in nums:
            if n not in hsh:
                hsh[n] = n - 1 
        
        print(hsh)

        seq = 0

        for h in hsh:
            if hsh[h] not in hsh: # if value (which is key - 1) isn't in dict
                # h is start of seq
                curr = h 
                nxt = curr + 1
                score = 1 
                while True:
                    if nxt in hsh:
                        score += 1
                        nxt += 1
                    else:
                        break
                if score > seq:
                    seq = score                        
        
        return seq
