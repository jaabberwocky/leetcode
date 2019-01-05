class Deque:

    def __init__(self):
        self.items = []

    def addFront(self, item):
        self.items.insert(0, item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop(len(self.items)-1)

    def isEmpty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

    def __repr__(self):
        return "Deque of %d items" % self.size()