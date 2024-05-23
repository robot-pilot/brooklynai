class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BST:
	def __init__(self):
		self.root = None

	def insert(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._insert(self.root, data)

	def _insert(self, node, data):
		if data < node.data:
			if node.left is None:
				node.left = Node(data)
			else:
				self._insert(node.left, data)

		else:
			if node.right is None:
				node.right = Node(data)
			else:
				self._insert(node.right, data)

	def inorder_traversal(self):
		elements = []
		self._inorder_traversal(self.root, elements)
		return elements

	def _inorder_traversal(self, node, elements):
		if node:
			self._inorder_traversal(node.left, elements)
			elements.append(node.data)
			self._inorder_traversal(node.right, elements)

	def search(self, target):
		res = self._search(self.root, target)
		if res == None:
			print(f"{target} not found")
		else:
			print(f"found: {res.data}")

	def _search(self, node, target):
		if node is None or node.data == target:
			return node
		if target < node.data:
			return self._search(node.left, target)
		else:
			return self._search(node.right, target)

if __name__ == "__main__":
	bst = BST()
	bst.insert(4)
	bst.insert(12)
	bst.insert(3)
	bst.insert(55)
	bst.insert(4)
	bst.insert(19)
	bst.insert(102)
	bst.insert(20)

	print(bst.inorder_traversal())

	bst.search(55)
	bst.search(5)
