from Stack import MyStack


def next_greater_element(lst):
    stack = MyStack()
    res = [None] * len(lst)

    for i in range(len(lst) - 1, -1, -1):
        # iterate backwards
        while not stack.is_empty() and stack.peek() <= lst[i]:
            stack.pop()

        if not stack.is_empty():
            # use the top element as nge if available
            res[i] = stack.peek()
        else:
            res[i] = -1
        stack.push(lst[i])
    return res
