def golf_score_calculator(par_string, score_string) -> int:
    score = 0
    for i in range(len(par_string)):
        score += int(score_string[i]) - int(par_string[i])
    return score