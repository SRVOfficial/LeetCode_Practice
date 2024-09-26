# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def preorder(node):
            if not node:
                return ""

            # Start with the node value
            result = str(node.val)
            
            # If there's a left child, recursively call and add parentheses
            if node.left:
                result += "(" + preorder(node.left) + ")"
            
            # If there's no left child but there's a right child, we need to add () for the left child
            elif node.right:
                result += "()"
            
            # If there's a right child, recursively call and add parentheses
            if node.right:
                result += "(" + preorder(node.right) + ")"
            
            return result

        # Start preorder traversal from root
        return preorder(root)