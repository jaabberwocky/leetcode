def check_exam(ans, student) -> int:
    score = 0
    for ind, val in enumerate(student):
        if len(val) == 0:
            continue
        elif val == ans[ind]:
            score += 4
        else:
            score -= 1
    if score < 0:
        score = 0
    return score