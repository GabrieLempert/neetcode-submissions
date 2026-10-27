class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        l = []
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] +=1
        sorted_items = sorted(d.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]
            

        

        





            



                
            
            

            


                

            


            