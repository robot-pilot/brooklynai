class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		last = self.head
		while last.next:
			last = last.next
		last.next = new_node
		new_node.prev = last

	def prepend(self, data):
		new_node = Node(data)
		if not self.head:
			self.head = new_node
			return
		self.head.prev = new_node
		new_node.next = self.head
		self.head = new_node

	def insert(self, data, pos):
		new_node = Node(data)

		if pos == 0:
			if not self.head:
				self.head = new_node
				return
			self.head.prev = new_node
			new_node.next = self.head
			self.head = new_node
			return 

		temp = self.head
		idx = 0

		while temp and idx < pos - 1:
			temp = temp.next
			idx += 1

		if temp is None or (temp.next is None and idx < pos - 1):
			print('pos out of bounds')
			return

		new_node.next = temp.next
		if temp.next:
			temp.next.prev = new_node
		temp.next = new_node
		new_node.prev = temp

	def delete(self, key):
		temp = self.head
		
		if not temp:
			return
		
		if temp and temp.data == key:
			self.head = temp.next
			if self.head:
				self.head.prev = None
			temp = None
			return

		while temp and temp.data != key:
			temp = temp.next

		if temp is None:
			print('key not found')
			return

		if temp.next:
			temp.next.prev = temp.prev

		if temp.prev:
			temp.prev.next = temp.next

		temp = None

	def display(self):
		temp = self.head
		while temp:
			print(temp.data, end=' ')
			temp = temp.next
		print('Done')


if __name__ == "__main__":
	dll = DoublyLinkedList()
	dll.append(5)
	dll.append(6)
	dll.prepend(4)
	dll.prepend(3)
	dll.append(7)
	dll.insert(4.5, 3)
	dll.delete(7)
	dll.delete(4.5)
	dll.display()
