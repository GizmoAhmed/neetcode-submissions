class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1

        final = []
        i = k 
        while i != 0:
            max_key = max(count, key=count.get)
            final.append(max_key)
            print("max_key: " + str(max_key) + " count[max_key]: " + str(count[max_key]))
            del count[max_key]
            i-=1

        return final
