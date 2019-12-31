class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = {}
        
        # populate dictionary of key:value pairs
        for num in arr:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        # check if values are unique
        s = set()
        for i, (key, val) in enumerate(d.items()):
            if val not in s:
                s.add(val)
            else:
                return False
            
        return True