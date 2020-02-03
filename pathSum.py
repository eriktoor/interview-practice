# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class SolutionPathSum:
    """
    Find if there is a path that adds up to a certain sum 
    https://leetcode.com/problems/path-sum/
    """
    def hasPathSum(self, root, sum):
        if not root: return False
        
        elif root.left == None and root.right == None: 
            return True if sum - root.val == 0 else False
        else: 
            return self.hasPathSum(root.left, sum - root.val) or self.hasPathSum(root.right, sum-root.val)
        
    def allPaths(self, root, res, cost): 
        if root.left == None and root.right == None: 
            res.append(cost + root.val)
        elif root.left != None and root.right != None: 
            self.allPaths(root.left, res, cost + root.val) 
            self.allPaths(root.right, res, cost + root.val)             
        elif root.left != None: 
            self.allPaths(root.left, res, cost + root.val) 
        elif root.right != None: 
            self.allPaths(root.right, res, cost + root.val) 
            
class SolutionPathSum2:
    """
    Find all paths that add up to a sum
    https://leetcode.com/problems/path-sum-ii/
    """
    def pathSum(self, root, sum):
        ans = []
        self.dfs(root, sum, [],ans)
        return ans

    def dfs(self, root, sum, tmp, ans):
        if not root:
            return

        if root.left == None and root.right == None and sum == root.val:
            ans.append(tmp+[root.val])
            return

        self.dfs(root.left, sum-root.val, tmp+[root.val], ans)
        self.dfs(root.right, sum-root.val, tmp+[root.val], ans)


class SolutionPathSum3:
    """
    Number of paths that sum to a given value 
    https://leetcode.com/problems/path-sum-iii/
    """
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # define global return var
        self.numOfPaths = 0
        # 1st layer DFS to go through each node
        self.dfs(root, target)
        # return result
        return self.numOfPaths
    
    # define: traverse through the tree, at each treenode, call another DFS to test if a path sum include the answer
    def dfs(self, node, target):

        if node is None:
            return 
        # dfs break down 
        self.test(node, target) # you can move the line to any order, here is pre-order
        self.dfs(node.left, target)
        self.dfs(node.right, target)
        
    def test(self, node, target):

        if node is None:
            return
        if node.val == target:
            self.numOfPaths += 1
            
        self.test(node.left, target-node.val)
        self.test(node.right, target-node.val)