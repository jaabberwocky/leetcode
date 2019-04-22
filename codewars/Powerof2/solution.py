def power_of_two(x):
    pow = 0
    
    while True:
        if 2 ** pow == x:
            return True
        elif 2 ** pow > x:
            return False
        else:
            pow += 1
    
            