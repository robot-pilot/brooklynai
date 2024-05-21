class Node:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key


root = Node(1)

root.left = Node(2)
root.right = Node(3)
lft = root.left
lft.left = Node(4)
lft.right = Node(5)
# nxt = lft.right
# nxt.left = Node(6)
# nxt.right = Node(7)

def inorder_traversal(root):
	if root:
		inorder_traversal(root.left)
		print(root.val, end=' ')
		inorder_traversal(root.right)

print("inorder_traversal: ", end=' ')
inorder_traversal(root)
print()

def preorder_traversal(root):
	if root:
		print(root.val, end=' ')
		preorder_traversal(root.left)
		preorder_traversal(root.right)

print("preorder_traversal: ", end=' ')
preorder_traversal(root)
print()

def postorder_traversal(root):
	if root:
		postorder_traversal(root.left)
		postorder_traversal(root.right)
		print(root.val, end=' ')

print("postorder_traversal: ", end=' ')
postorder_traversal(root)
print()

class BSTNode:
	def __init__(self, key):
		self.left = None
		self.right = None
		self.val = key

	def insert(self, key):
		if self.val:
			if key < self.val:
				if self.left is None:
					self.left = BSTNode(key)
				else:
					self.left.insert(key)

			elif key > self.val:
				if self.right is None:
					self.right = BSTNode(key)
				else:
					self.right.insert(key)

		else:
			self.val = key

	def search(self, key):
		if key < self.val:
			if self.left is None:
				return f"{key} not found"
			return self.left.search(key)
		elif key > self.val:
			if self.right is None:
				return f"{key} not found"
			return self.right.search(key)
		else:
			return f"{key} found"



test = BSTNode(10)
test.insert(6)
test.insert(14)
test.insert(3)
test.insert(8)
test.insert(7)
test.insert(4)
test.insert(13)
test.insert(15)

print(test.search(7))
print(test.search(14))

inorder_traversal(test)

def print_tree(node, level=0, label='.'):
	indent = ' ' * (4 * level) + label + '---'
	if node is not None:
		print(f"{indent}{node.val}")
		if node.left is not None or node.right is not None:
			print_tree(node.left, level + 1, 'L')
			print_tree(node.right, level + 1, 'R')
	else:
		print(f"{indent}None")

print("Binary Search Tree:")
print_tree(test)

def display(node, space=0, level=0, label='Root'):
	# Base case: empty node
	if node is None:
		return

	# Increase distance between levels
	space += 10

	# Process right child first
	display(node.right, space, level + 1, 'R')

	# Print current node after space
	print()
	for i in range(10, space):
		print(' ', end='')
	print(f'{label}: {node.val}')

	# Process left child
	display(node.left, space, level + 1, 'L')

display(test)
