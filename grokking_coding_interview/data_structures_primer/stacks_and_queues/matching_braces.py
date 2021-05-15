from Stack import MyStack


def is_balanced(exp):
    if len(exp) == 0:
        return True
    stack = MyStack()
    braces = {
        "{": "}",
        "[": "]",
        "(": ")"
    }
    for ch in exp:
        if ch in braces:
            stack.push(ch)
        else:
            # closers
            if braces[stack.pop()] != ch:
                return False
    return True


class Test:

    def test_1(self):
        assert is_balanced('{[()]}') is True

    def test_2(self):
        assert is_balanced('[{(}]') is False

    def test_3(self):
        assert is_balanced('({[}])') is False

    def test_4(self):
        assert is_balanced('[{}]') is True

    def test_5(self):
        assert is_balanced('') is True