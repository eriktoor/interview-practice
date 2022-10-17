"""
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        ret = []
        
        def inOrder(node):
            if node:
                inOrder(node.left)
                ret.append(node.val)
                inOrder(node.right)
                
        inOrder(root)
        return ret == sorted(ret) and len(set(ret)) == len(ret)

"""


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
