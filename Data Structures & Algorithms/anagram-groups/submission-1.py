class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq = [0]*26
        d = dict()
        li = []
        for s in strs:
            for c in s:
               freq[ord(c) - ord('a')] += 1
            key = tuple(freq)
            if key not in d:
                d[key] = [s]
            else:
                d[key].append(s)
            freq = [0]*26
        for k in d:
            li.append(d[k])
        return li