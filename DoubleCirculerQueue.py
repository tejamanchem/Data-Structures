
class Deque:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return self.items==[]

    def addRear(self,item):
        self.items.append(item)

    def addFront(self,item):
        self.items.insert(0,item)

    def removeFront(self):
        self.items.pop(0)

    def removeRear(self):
        self.items.pop()

    def sizeof(self):
        return len(self.items)

newDeque = Deque()
newDeque.addFront(12)
newDeque.addFront(13)
newDeque.addFront(14)
newDeque.addRear(11)
newDeque.addRear(10)
newDeque.removeFront()
newDeque.removeRear()

print(newDeque.items)
print(newDeque.sizeof())

