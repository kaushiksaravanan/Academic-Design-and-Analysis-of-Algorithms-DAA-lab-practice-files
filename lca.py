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


def lca(root,n1,n2):
	if root:
		if root.val<n1 and root.val<n2:
			return lca(root.right,n1,n2)
		if root.val>n1 and root.val>n2:
			return lca(root.left,n1,n2)
		else:
			return root.val

# n=[int(i) for i in input().split()]
n=[20,8,22,4,12,10,14] 	

root=None
for i in range(len(n)):
	root=bst_insert(root,n[i])


n=[int(i) for i in input().split()]
print(lca(root,n[0],n[1]))

# TC log(n)
# SC n