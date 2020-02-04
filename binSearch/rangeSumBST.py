# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

"""
Approaches: 

Approach 1: Using the BST invariant 

find the left value in log(n) time 
    increment left along way 
find the right value in log(n)time 
    increment right along way 

ret = left + right + root 

Time: O(log(n)), Space: O(1)

"""

class Solution:
    def __init__(self):
        self.sum = 0     
        self.ret = 0
    def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
        """
        @desc find the sum of the values between the L and R values in a BST, including those values
        @args 
            @arg1 root which is your starting node
            @arg2 L value which is one of your target values
            @arg3 R value which is your other target value
        @return ret which is an integer showing the sum of the values between L and r
        """
        ret = []
        def inOrder(root): 
            if root: 
                inOrder(root.left)
                if L <= root.val <= R:
                    ret.append(root.val)
                inOrder(root.right)
        
        inOrder(root)
        return sum(ret)
    def rangeSumBST2(self, root: TreeNode, L: int, R: int) -> int:
        """
        @desc find the sum of the values between the L and R values in a BST, including those values
        @args 
            @arg1 root which is your starting node
            @arg2 L value which is one of your target values
            @arg3 R value which is your other target value
        @return ret which is an integer showing the sum of the values between L and r
        """
        def inOrder(root): 
            if root: 
                inOrder(root.left)
                if L <= root.val <= R:
                    self.ret += root.val
                inOrder(root.right)
        
        inOrder(root)
        return self.ret
    def rangeSumBST3(self, root: TreeNode, L: int, R: int) -> int:
        """
        @desc find the sum of the values between the L and R values in a BST, including those values
        @args 
            @arg1 root which is your starting node
            @arg2 L value which is one of your target values
            @arg3 R value which is your other target value
        @return ret which is an integer showing the sum of the values between L and r
        """
        ret = {}
        ret["ans"] = 0
        def inOrder(root): 
            if root: 
                inOrder(root.left)
                if L <= root.val <= R:
                    ret["ans"] += root.val
                inOrder(root.right)
        
       
        inOrder(root)
        return ret["ans"]
    def rangeSumBST(self, root, L, R): 
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                if L < node.val:
                    dfs(node.left)
                if node.val < R:
                    dfs(node.right)

        self.ans = 0
        dfs(root)
        return self.ans
    
    
    
    
    
    
    
    
    