def findOnlyOneOccur(words):
    wordcount = {}
    onlyone = []
    
    for w in words.split(" "):
        if w not in wordcount:
            wordcount[w] = 1
        else:
            wordcount[w] += 1
    
    for v in wordcount.items():
        if v[1] == 1:
            onlyone.append(v[0])
    
    return onlyone

class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """    
        Aonlyone = findOnlyOneOccur(A)
        Bonlyone = findOnlyOneOccur(B)
        
        uncommon = []
        
        for w in Aonlyone:
            if w not in B.split(" "):
                uncommon.append(w)
        for w in Bonlyone:
            if w not in A.split(" "):
                uncommon.append(w)
        return uncommon
    