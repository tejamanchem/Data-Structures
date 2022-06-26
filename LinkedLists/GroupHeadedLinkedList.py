
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = Node(0)
		self.last_node = self.head

	def append(self, data):
		self.last_node.next = Node(data)
		self.last_node = self.last_node.next

	def display(self):
		current = self.head.next
		while current is not None:
			print(current.data, end=' ')
			current = current.next
		print()


if __name__ == '__main__':
	L = LinkedList()
	L.append(1)
	L.append(2)
	L.append(3)
	L.append(4)
	L.display()
