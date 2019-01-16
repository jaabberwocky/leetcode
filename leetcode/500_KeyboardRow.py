class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        firstrow = set("qwertyuiop")
        secondrow = set("asdfghjkl")
        thirdrow = set("zxcvbnm")
        
        listRows = [firstrow, secondrow, thirdrow]
        oneRow = []
        
        for w in words:
            for r in listRows:
                if r.issuperset(set(w.lower())):
                    oneRow.append(w)
        
        return oneRow