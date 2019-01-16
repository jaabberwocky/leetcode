'''
URL: https://leetcode.com/problems/jewels-and-stones/description/
Desc: You're given strings J representing the types of stones that are jewels, and S representing the stones you have.  Each character in S is a type of stone you have.  You want to know how many of the stones you have are also jewels.

The letters in J are guaranteed distinct, and all characters in J and S are letters. Letters are case sensitive, so "a" is considered a different type of stone from "A".
'''

class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        from collections import Counter
        ctr = Counter(S)
        
        sum = 0
        for key in ctr.keys():
            if key in J:
                sum += ctr[key]
        return sum
        