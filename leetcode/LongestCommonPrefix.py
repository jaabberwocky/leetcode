# https://leetcode.com/problems/longest-common-prefix/

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_prefix = ""
        min_length = self.get_min_length_from_list(strs)
        i = 0
        
        while i < min_length:
            ch = None
            for s in strs:
                if ch is None:
                    ch = s[i]
                elif s[i] != ch:
                    return common_prefix
            common_prefix += ch
            i += 1
            
        return common_prefix
                
        
    def get_min_length_from_list(self, strs):
        min_length = None
        for s in strs:
            if min_length is None:
                min_length = len(s)
            elif len(s) < min_length:
                min_length = len(s)
        return min_length