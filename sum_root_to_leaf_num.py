# Time Complexity : O(n)
# Space Complexity : O(h); h -- height of the tree.
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No

# Iterative Approach
class Solution:
    
    def __init__(self):
        self.sum = 0
        self.val = 0
        self.stack = []
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        while root or self.stack:
            while root:
                if root is None:
                    return
                
                self.val = (self.val * 10) + root.val
                self.stack.append([root, self.val])
                root = root.left
                
            pop = self.stack.pop()
            root = pop[0]    
            if root.left is None and root.right is None:
                self.sum += self.val
            self.val = pop[1]
            root = root.right
        return self.sum





# recursive method
class Solution:
    
    def __init__(self):
        self.sum = 0
    
    def helper(self, root, temp):
        if root is None:
            return
        if root.left is None and root.right is None:
            self.sum += (root.val + temp*10)
       
        self.helper(root.left, temp * 10 + root.val) 
        self.helper(root.right, temp * 10 + root.val)
        
        
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.helper(root, 0)
        return self.sum
