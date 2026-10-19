class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        front = numbers[i]
        back = numbers[j]
        while front + back != target:
            if front + back < target:
                i += 1
            elif front + back > target:
                j -= 1
            front = numbers[i]
            back = numbers[j]
        
        return [i + 1, j + 1]
        