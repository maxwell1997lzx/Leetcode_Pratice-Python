class Node(object): # First step is to defind the data struture, which is the node
    def __init__(self, val, left=None, right=None): # Come up with the constructor which take in the value, the left side node and right side node.
        self.val = val
        self.left = left
        self.right = right # Next, assign these nodes

# Then come up with a solution class
class Solution(object):
    def _isValidBSTHelper(self, n, low, high): # Using helperfunction to pass into low and high values as parameters. which is def _isValidBSTHelper with given node, the low value and high value
        if not n:
            return True
        # Then fillout is _validBSTHelper.  
        val = n.val 
        if ((val > low and val < high) and # get the value and check that if the value is greater than the low value and less than the high value
            self._isValidBSTHelper(n.left, low, n.val) and # check if the value on the left sub tree is in the given range which is from low to n.val
            self._isValidBSTHelper(n.right, n.val, high)): # check if the value on the right sub tree is within the range resriction being on the current value to the high value
            return True
        return False
        
    def isValidBST(self, n): # Using the main function def isValid with Binary Search Tree(isValidBST) and given a node
        return self._isValidBSTHelper(n, float('-inf'), float('inf')) # And I also passing low and high value with the float of negative infinity and positive infinity
        
# Then come up with test functions for this
#    5
#   / \
#  4   7
node = Node(5)
node.left = Node(4)
node.right = Node(7)
print(Solution().isValidBST(node))

#    5
#   / \
#  4   7
#     / \ 
#    6   8
node = Node(5)
node.left = Node(4)
node.right = Node(7)
node.right.left = Node(6)
node.right.right = Node(8)
print(Solution().isValidBST(node))

#       10
#       / \
#      5   15
#     / \  /  \
#    2   7 13  18  
#        \ /    \
#        9 11
#        \
