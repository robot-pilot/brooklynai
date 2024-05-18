class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class SinglyLinkedList:
	def __init__(self):
		self.head = None

	def insert_at_beginning(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def inset_at_end(self, data):
		new_node = Node(data)
		if self.head is None:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node

	def delete_node(self, key):
		temp = self.head

		if temp is not None:
			if temp.data == key:
				self.head = temp.next
				temp = None
				return

		while temp is not None:
			if temp.data == key:
				break
			prev = temp
			temp = temp.next

		if temp == None:
			return

		prev.next = temp.next
		temp = None

	def search(self, key):
		current = self.head
		while current is not None:
			if current.data == key:
				return True
			current = current.next
		return False

	def print_list(self):
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next
		print()

llist = SinglyLinkedList()
llist.insert_at_beginning(1)
llist.inset_at_end(2)
llist.inset_at_end(3)
llist.print_list()

llist.delete_node(2)
llist.print_list()

print(llist.search(3))
print(llist.search(4))
