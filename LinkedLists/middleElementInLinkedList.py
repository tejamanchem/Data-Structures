
class Node:
	def __init__(self, value):
		self.data = value
		self.next = None
	
class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, new_data):
		new_node = Node(new_data)
		new_node.next = self.head
		self.head = new_node
		
	def printMiddle(self):
		temp = self.head
		count = 0
		
		while self.head:
			if (count & 1):
				temp = temp.next
			self.head = self.head.next
			count += 1
		print(temp.data)	
		

llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)

llist.printMiddle()
