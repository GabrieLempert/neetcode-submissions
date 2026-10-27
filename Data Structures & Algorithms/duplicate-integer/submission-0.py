class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
       new_numbers = dict()
       for num in nums:
        if num not in new_numbers:
            new_numbers[num]= 0
        else:
            new_numbers[num]+=1

       for num in nums:
            if new_numbers[num] > 0:
                return True

       return False 
        
    

        
        
            