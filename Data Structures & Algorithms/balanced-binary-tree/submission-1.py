# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(root):
            
            if not root: #base case, stops the recursion
                return[True, 0]

            left_side, right_side = dfs(root.left), dfs(root.right) #per node, gets outcome
            balanced = (left_side[0] and right_side[0]) and abs(left_side[1] - right_side[1]) <= 1
            #decides if "empty" at bottom and balanced

            return [balanced, 1 + max(left_side[1], right_side[1])] #if balanced, height difference

        return dfs(root)[0] #only need bool




        