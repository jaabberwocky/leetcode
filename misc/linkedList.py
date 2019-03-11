class Node:
    next = None
    data = None
    
    def __init__(self, data):
        self.data = data

class LinkedList:
    head = None

    def __init__(self, data):
        self.head = Node(data)

    def addHead(self, data):
        old = self.head
        new = Node(data)
        new.next = old
        self.head = new
    
    def __repr__(self):
        point = self.head
        while point.next != None:
            print("Node: %s" % str(point.data))
            point = point.next

    def __str__(self):
        point = self.head
        returnedString = "**Head**\n"
        while point is not None:
            returnedString += "Node: %s\n" % str(point.data)
            point = point.next
        return returnedString + "**Tail**"
        

if __name__ == "__main__":
    l = LinkedList(45)
    l.addHead(50)
    l.addHead("jimmy")
    l.addHead(111.123)
    print(l)
