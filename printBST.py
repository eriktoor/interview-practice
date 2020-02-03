

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class SolutionLevelOrder:
    """
https://leetcode.com/problems/binary-tree-level-order-traversal/submissions/

https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

    """

    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root == None: return []
        
        res = [] 
        
        import queue
        S = queue.Queue()
        
        S.put(root)
        
        while S.qsize() != 0: 
            currLevel = []
            
            for i in range(S.qsize()):
                curr = S.get()
                currLevel.append(curr.val)
                if curr.left != None: 
                    S.put(curr.left)
                if curr.right != None: 
                    S.put(curr.right)     
                    
            res.append(currLevel)
                
        return res 
        
        
        
        

class SolutionPrintBST:
    """
    https://leetcode.com/problems/print-binary-tree/discuss/106273/Simple-Python-with-thorough-explanation

    Given a Binary Tree of height H:

    The maximum total number of nodes is = 2^H - 1
    Number of nodes at each level, L (0-indexed) = 2^L
    We can view the final output as a 2-D matrix, where the number of rows is the height of the tree and the number of columns will be the 2^H - 1.

    Taking this tree as example:

            1
        /   \\
        2      3
    /  \    / \\
    4   5   6   7
    / \\
    8   9
    Our final matrix should look like this:

    .......1....... <- Level 0, Left padding: 7, Spacing: 15
    ...2.......3... <- Level 1, Left padding: 3, Spacing: 7
    .4...5...6...7. <- Level 2, Left padding: 1, Spacing: 3
    8.9............ <- Level 3, Left padding: 0, Spacing: 1


    """
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        rows = get_height(root)
        cols = 2 ** rows - 1
        res = [['' for _ in range(cols)] for _ in range(rows)]

        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            print(level, index, node.val)
            res[level][index] = str(node.val)
            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)
        traverse(root, 0, 0)
        return res


def printInorder(root): #left, root, right
    if root: 
        # First recur on left child 
        printInorder(root.left) 
        # then print the data of node 
        print(root.val), 
        # now recur on right child 
        printInorder(root.right) 
  
def printPostorder(root): #left, right, root 
    if root:
        printPostorder(root.left) 
        printPostorder(root.right) 
        print(root.val), 
  
def printPreorder(root): #root, left, right
    if root: 
        print(root.val)
        printPreorder(root.left) 
        printPreorder(root.right) 



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionIsSubtree:
    def isMatch(self, s, t):
        if not(s and t):
            return s is t
        return (s.val == t.val and 
                self.isMatch(s.left, t.left) and 
                self.isMatch(s.right, t.right))

    def isSubtree(self, s, t):
        if self.isMatch(s, t): return True
        if not s: return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)        