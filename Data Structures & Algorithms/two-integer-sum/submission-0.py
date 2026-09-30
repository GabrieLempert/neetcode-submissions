class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        sum = dict()
        l = []
        for i, num in enumerate(nums):
            compli = target - num
            if compli in sum:
                return [sum[compli], i]
            else:
                sum[num] = i
        
        return l
                
    
