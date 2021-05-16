from Stack import MyStack


def evaluate_post_fix(exp):
    ops = ["+", "*", "-", "/"]
    stack = MyStack()

    for el in exp:
        if el == " ":
            continue
        elif el in ops:
            v1, v2 = stack.pop(), stack.pop()
            res = eval(f"{v2} {el} {v1}")
            stack.push(res)
        else:
            stack.push(el)
    final_num = int(stack.pop())
    return final_num


class Test:

    def test_1(self):
        exp = "921 * - 8 - 4 +"
        assert evaluate_post_fix(exp) == 3

    def test_2(self):
        exp = "9, 4, 2, +, *, 6, 14, 7, /, +, *".replace(",", "")
        print(evaluate_post_fix(exp))