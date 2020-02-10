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


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# https://leetcode.com/problems/binary-tree-maximum-path-sum/

class maxPathSum:
    def maxPathSum(self, root: TreeNode) -> int:
        maxPath = []
        def inorder(root):
            if root: 
                maxPath.append(root.val)
                inorder(root.left)
                inorder(root.right)
        
        inorder(root)
        
        total_sum = maxPath[0]
        current_sum = maxPath[0]
        print(maxPath)
        for i in range(1, len(maxPath)): 
            current_sum = max(current_sum + maxPath[i], maxPath[i])
            total_sum = max(current_sum, total_sum)
        
        return total_sum
    
    def maxPathSum(self, root: TreeNode) -> int:
        max_path_sum = {}
        max_path_sum["ans"] = root.val
        def helper(node): 
            if node == None: return 0 
            left = max(0, helper(node.left))
            right = max(0, helper(node.right))
            max_path_sum["ans"] = max(max_path_sum["ans"], left + right + node.val)
            return max(left, right) + node.val
            
        helper(root)
        return max_path_sum["ans"]


class Solution:               
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/solution/
    
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        def helper(in_left = 0, in_right = len(inorder)):
            nonlocal pre_idx
            # if there is no elements to construct subtrees
            if in_left == in_right:
                return None
            
            # pick up pre_idx element as a root
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)

            # root splits inorder list
            # into left and right subtrees
            index = idx_map[root_val]

            # recursion 
            pre_idx += 1
            # build left subtree
            root.left = helper(in_left, index)
            # build right subtree
            root.right = helper(index + 1, in_right)
            return root
        
        # start from first preorder element
        pre_idx = 0
        # build a hashmap value -> its index
        idx_map = {val:idx for idx, val in enumerate(inorder)} 
        return helper()