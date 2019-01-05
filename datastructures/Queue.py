class Queue:
# python3 implementation of Queue, expecting either a single primitive or list of primitives

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        if len(item) == 0:
            raise ValueError("Item cannot be empty.")
        elif len(item) == 1:
            self.items.append(item)
        else:
            for i in item:
                self.items.append(i)

    def dequeue(self):
        return self.items.pop(0)

    def isEmpty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __repr__(self):
        return "Queue of %d items" % self.size()
