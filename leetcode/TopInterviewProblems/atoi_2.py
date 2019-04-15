class Solution:
    def myAtoi(self, str: str) -> int:
        ISNEGATIVE = False
        digits = []
        
        # remove whitespace
        s = str.strip().lower()
        if len(s) == 0:
            return 0
        
        if s[0] in ['-', '+']:
            if s[0] == '-':
                ISNEGATIVE = True
            s = s[1:]
        
        for ch in s:
            if ch not in '0123456789':
                # covers case where first non-whitespace character is not a digit
                if len(digits) == 0:
                    return 0
                else:
                    break
            else:
                digits.append(ch)
        
        # return non-valid if nothing else was found
        if len(digits) == 0:
            return 0
        
        # check if num is within range
        if ISNEGATIVE:
            num = -int(''.join(digits))
        else:
            num = int(''.join(digits))
            
        if num < -2**31:
            return -2**31
        elif num > (2**31) - 1:
            return 2**31 - 1
        else:
            return num
    