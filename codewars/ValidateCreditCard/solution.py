def validate(n):

    digits = [int(d) for d in str(n)[::-1]]
    ctr = 1
    
    for ind, digit in enumerate(digits):
        if ind == 0:
            continue
        if ind == ctr:
            digit *= 2
            if digit > 9:
                digit -= 9
            digits[ind] = digit
            ctr += 2
    
    return sum(digits) % 10 == 0


if __name__ == "__main__":
    t1 = 2121
    rs = validate(2121)
    try:
        assert rs==True
    except AssertionError:
        print("Code is incorrect!")