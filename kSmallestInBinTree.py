
class kSmallestInBinTree:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        #only want to remember result and which element we are at 
        nums = [0,0] #where we are, value
        
        def inOrder(root, nums, k): 
            if not root: return 
            
            inOrder(root.left, nums, k)
            nums[0] += 1
            if nums[0] == k:
                nums[1] = root.val
                return
            inOrder(root.right, nums, k)
            
        inOrder(root, nums, k)     
        return nums[1]
        
    
    def kthSmallestNspace(self, root: TreeNode, k: int) -> int:
        """N SPACE"""
        
        
        def inOrder(root): 
            
            if root: 
                inOrder(root.left)
                order.append(root.val)
                inOrder(root.right)
        
        order = []
        
        inOrder(root)
        return order[k-1]
            