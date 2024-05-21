class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
	
	def prepend(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		new_node.next = self.head
		self.head.prev = new_node
		self.head = new_node

	def append(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
		new_node.prev = last

	def delete_node(self, key):
		temp = self.head
		while temp:
			if temp.data == key:
				if temp.prev:
					temp.prev.next = temp.next
				if temp.next:
					temp.next.prev = temp.prev
				if temp == self.head:
					self.head = temp.next
				temp = None
				return
			temp = temp.next

	def display(self):
		node = self.head
		while node:
			print(node.data, end=" ")
			node = node.next
		print()

dll = DoublyLinkedList()
dll.prepend(3)
dll.prepend(2)
dll.prepend(1)
dll.prepend(4)
dll.display()

dll.append(4)
dll.append(5)
dll.display()

dll.delete_node(3)
dll.display()
