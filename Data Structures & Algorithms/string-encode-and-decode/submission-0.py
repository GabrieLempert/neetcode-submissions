class Solution:

    def encode(self, strs: List[str]) -> str:
        return "".join(f"{len(s)}#{s}" for s in strs)
            

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        
        while i < len(s):
            # 1. Locate the delimiter '#' that follows the length digits
            j = s.find('#', i)
            
            # 2. Extract the length from between index i and index j
            length = int(s[i:j])
            
            # 3. Read the exact number of characters starting after '#'
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            # 4. Jump i directly to the start of the next length prefix
            i = end
            
        return res



