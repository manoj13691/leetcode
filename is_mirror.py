class Node:
	def __init__(self, val):
		self.val = val
		self.right = None
		self.left = None
		self.left_array =[]
		#self.right_array = []

	def inorder(self, root):
		if root == None:
			return 
		self.inorder(root.left)
		#print(root.val)
		self.left_array.append(root.val)
		self.inorder(root.right)

	def weirdOrder(self, root):
		if root == None:
			return
		a = self.weirdOrder(root.right)
		#print(root.val)
		#self.right_array.append(root.val)
		popped_element = self.left_array.pop(0)
		print(popped_element)
		if popped_element != root.val:
			return False
		b = self.weirdOrder(root.left)


		if a==False or b==False:
			return False
		else:
			return True


def isMirror(r1, r2):
	if r1 == None and r2!= None:
		return False

	elif r1!=None and r2==None:
		return False

	elif r1==None and r2==None:
		return True

	else:

		if r1.val == r2.val:
			return isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)
		else:
			return False



root = Node(1)
root.left = Node(2)
root.right = Node(2)

root.left.left = Node(4)
root.left.right = Node(4)

root.right.left = Node(4)
root.right.right = Node(3)

#root.inorder(root.left)
#print("\n")
#print(root.weirdOrder(root.right))

print(isMirror(root.left, root.right))






