class Node(object):
	def __init__(self, val):
		self.left=None
		self.right=None
		self.val=val

def bst_insert(root,key):
	if root is None:
		return Node(key)
	else:
			if root.val<key:
				root.right=bst_insert(root.right,key)
			elif root.val>key:
				root.left=bst_insert(root.left,key)
	return root

a=[]
def inorder(root):
	if root:
		inorder(root.left)
		a.append(root.val)
		inorder(root.right)

n=[int(i) for i in input().split()]
k=int(input("Nth largest element"))

r=None
for i in range(len(n)):
	r=bst_insert(r,n[i])

inorder(r)
print('Inorder traversal')
print(*a)
print('The kth largest element is')
print(a[-k])
