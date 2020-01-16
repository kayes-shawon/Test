""" Program to find LCA of node1 and node2 using one traversal of 
Binary tree 
It handles all cases even when node1 or node2 is not there in tree 
"""

# A binary tree node 
class Node: 

	# Constructor to create a new node 
	def __init__(self, key): 
		self.key = key 
		self.left = None
		self.right = None
		
def findLCAUtil(root, node1, node2, v): 
	"""
	Additional function to traverse through tree
	"""
	# Base Case 
	if root is None: 
		return None
	if root.key == node1 : 
		v[0] = True
		return root 

	if root.key == node2: 
		v[1] = True
		return root 

	# Look for keys in left and right subtree 
	left_lca = findLCAUtil(root.left, node1, node2, v) 
	right_lca = findLCAUtil(root.right, node1, node2, v) 

	# If both of the above calls return Non-NULL, then one key 
	# is present in once subtree and other is present in other, 
	# So this node is the LCA 
	if left_lca and right_lca: 
		return root 

	# Otherwise check if left subtree or right subtree is LCA 
	return left_lca if left_lca is not None else right_lca 


def find(root, k): 
	
	# Base Case 
	if root is None: 
		return False
	
	# If key is present at root, or if left subtree or right 
	# subtree , return true 
	if (root.key == k or find(root.left, k) or
		find(root.right, k)): 
		return True
	
	# Else return false 
	return False

def lca(root, node1, node2): 
	
	# Initialize node1 and node2 as not visited 
	v = [False, False] 

	lca = findLCAUtil(root, node1, node2, v) 

	# Returns LCA only if both node1 and node2 are present in tree 
	if (v[0] and v[1] or v[0] and find(lca, node2) or v[1] and
		find(lca, node1)): 
		return lca 

	# Else return None 
	return None

# Driver program to test above function 
root = Node(1) 
root.left = Node(2) 
root.right = Node(3) 
root.left.left = Node(4) 
root.left.right = Node(5) 
root.right.left = Node(6) 
root.right.right = Node(7) 
root.left.left.left = Node(8)
root.left.left.right = Node(9)

lca = lca(root, 3, 7) 

if lca is not None:
	print ("LCA(3, 7) = ", lca.key)
else : 
	print ("Keys are not present")
