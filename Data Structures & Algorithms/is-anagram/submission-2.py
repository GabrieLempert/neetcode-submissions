class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        d_1= dict()
        d_2 = dict()
        for letter in s:
            if letter in d_1:
                d_1[letter] += 1
            else:
                d_1[letter]= 0
        for letter in t:
            if letter not in d_1:
                return False
            if letter not in d_2:
                 d_2[letter]= 0
            else:
                d_2[letter] +=1
        
        for d in d_1:
            if d_1[d] != d_2[d]:
                return False
        
        return True



        