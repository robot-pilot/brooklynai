class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None
	
	def insert_at_beginning(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
		else:
			new_node.next = self.head
			self.head.prev = new_node
			self.head = new_node

	def insert_at_end(self, data):
		new_node = Node(data)
		if not self.head:
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

	def print_list(self):
		node = self.head
		while node:
			print(node.data, end=" ")
			node = node.next
		print()

dll = DoublyLinkedList()
dll.insert_at_beginning(3)
dll.insert_at_beginning(2)
dll.insert_at_beginning(1)
dll.insert_at_beginning(3)
dll.print_list()

dll.insert_at_end(4)
dll.insert_at_end(5)
dll.print_list()

dll.delete_node(3)
dll.print_list()
