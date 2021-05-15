from CustomQueue import MyQueue
from Stack import MyStack


def reverseK(queue, k):
    if k > queue.size() or k < 0 or queue.is_empty():
        return None

    stack = MyStack()
    new_q = MyQueue()

    for i in range(k):
        v = queue.dequeue()
        stack.push(v)

    while not stack.is_empty():
        v = stack.pop()
        new_q.enqueue(v)

    while not queue.is_empty():
        v = queue.dequeue()
        new_q.enqueue(v)

    return new_q

