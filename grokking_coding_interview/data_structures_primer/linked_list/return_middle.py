def find_mid(lst):
    slow, fast = lst.get_head(), lst.get_head()

    while fast.next_element is not None:
        slow = slow.next_element
        if not fast.next_element.next_element:
            return slow.data
        else:
            fast = fast.next_element.next_element
    return slow.data


class Test:

    def test_1(self):
        l = [7, 14, 10, 21]
        assert find_mid(l) == 14
