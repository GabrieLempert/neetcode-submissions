class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        d = dict()
        size = len(nums)
        temp = nums[0]
        d[temp] = 1
        for i in range(1,size):
            if nums[i] == temp:
                 d[nums[i]] += 1
            else:
                temp = nums[i]
                if nums[i] not in d:
                    d[nums[i]] = 1

        sorted_keys = sorted(d, key=lambda x: d[x], reverse=True)

            

        return sorted_keys[:k]


                
            
            

            


                

            


            