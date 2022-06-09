# structure of Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None


class LinkedList:
	def __init__(self):
		self.head = Node(0)
		self.last_node = self.head

	# function to add elements to header linked list
	def append(self, data):
		self.last_node.next = Node(data)
		self.last_node = self.last_node.next

	# function to print the content of header linked list
	def display(self):
		current = self.head.next
		# traversing the header linked list
		while current is not None:
			# at each node printing its data
			print(current.data, end=' ')
			# giving current next node
			current = current.next
		# print(self.head.data)
		print()


if __name__ == '__main__':
	L = LinkedList()
	# adding elements to the header linked list
	L.append(1)
	L.append(2)
	L.append(3)
	L.append(4)
	# displaying elements of header linked list
	L.display()
