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

n1=[int(i) for i in input().split()]
n2=[int(i) for i in input().split()]

if len(n1)!=len(n2):
	print('False')
	exit()
r1=None
for i in range(len(n1)):
	r1=bst_insert(r1,n1[i])

inorder(r1)
ino_r1=a[:]
a.clear()
# print(a,'cleared')

r2=None
for i in range(len(n2)):
	r2=bst_insert(r2,n2[i])
inorder(r2)
ino_r2=a
# print(ino_r2,a)

# print(ino_r2,ino_r1)
print(ino_r2==ino_r1)

#SC o(n)
#TC o(n)