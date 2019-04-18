def nb_dig(n, d):
    count = 0

    for i in range(n+1):
        k = i ** 2
        for ch in str(k):
            if ch == str(d):
                count += 1
    return count