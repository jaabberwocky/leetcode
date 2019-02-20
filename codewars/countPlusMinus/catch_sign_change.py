import sys

def catch_sign_change(lst):
    if len(lst) == 0:
        return 0
    
    positiveSign = None
    count = 0
    
    for d in lst:
        if positiveSign is None:
            positiveSign = d >= 0
        else:
            if positiveSign and d < 0:
                positiveSign = False
                count += 1
            elif positiveSign == False and d >= 0:
                positiveSign = True
                count += 1
    return count

if __name__ == "__main__":
    if len(sys.argv) <= 1:
        raise Exception("Incorrect number of arguments.")
    else:
        digits = []
        for d in sys.argv[1:]:
            try:
                digits.append(int(d))
            except ValueError:
                raise ValueError("Argument other than integer passed to script.")
        print("Count: %d" % catch_sign_change(digits))