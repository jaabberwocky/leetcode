class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        isPositive = True
        hasSign = False
        stringNum = ''
        
        # strip out whitespace
        s = s.lstrip()
        
        if len(s) == 0:
            return 0
        
        # check for sign
        if s[0] == '+' or s[0] == '-':
            hasSign = True
            if s[0] == '-':
                isPositive = False
        if hasSign:
            s = s[1:]
            
        if len(s) == 0:
            return 0
            
        for ch in s:
            if ch in '0123456789':
                stringNum += ch
            elif ch not in '0123456789' and len(stringNum) == 0:
                return 0
            else:
                break
        
        intNum = int(stringNum)
        if isPositive != True:
            intNum = - intNum
        if intNum >= 2**31:
            intNum = 2**31 - 1
        elif intNum < -2**31:
            intNum = -2**31
    
        return intNum
            
                