def remove(s, n):
    string = ""
    for ch in s:
        if ch == "!" and n > 0:
            n -= 1
            continue
        else:
            string+=ch
    return string