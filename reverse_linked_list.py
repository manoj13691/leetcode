class Node:

	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:

	def __init__(self):
		self.head = None

	def push(self, data):
		new_node = Node(data)
		new_node.next = self.head
		self.head = new_node

	def print(self):
		temp = self.head

		if temp == None:
			print("No elements")
			return

		while(temp != None):
			print(temp.data)
			temp = temp.next


def reverseLL(head):

	#print(head)

	if head.head == None:
		return head.head

	cur = head.head	
	prev = None

	while(cur is not None):
		next = cur.next
		cur.next = prev
		prev = cur
		cur = next
	return prev

if __name__ == '__main__':
	head_list = LinkedList()
	head_list.push(10)
	#head_list.push(20)
	#head_list.push(5)
	head_list.print()
	head_list.head = reverseLL(head_list)
	head_list.print()

