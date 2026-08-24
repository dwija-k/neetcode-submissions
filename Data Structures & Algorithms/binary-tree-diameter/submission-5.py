# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        max_diameter = 0  #storing result 

        def dfs(root):  #set up dfs function 
            nonlocal max_diameter  #allow local function to access global variable 

            if not root:  #base case, eventually stops recursion
                return 0   #if no roots, then longest path is 0 (doesn't exist)
            
            left_path = dfs(root.left)  #left side 
            right_path = dfs(root.right)  #right side 
            max_diameter = max(max_diameter, left_path + right_path)  #stores max of both; iteration

            return 1 + max(left_path, right_path)  #return depth (is dfs)

        dfs(root)  #recursive function on the root
        return max_diameter  #output