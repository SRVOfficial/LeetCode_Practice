# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        self.k = k
        self.result = None

        def dfs(node):
            # if node is None or we've already found the result
            if node is None or self.result:
                return

            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return

            dfs(node.right)

        dfs(root)
        return self.result

        # def inorder(root):
        #     res = []
        #     res = rInorder(root, res)
        #     return res[k-1]
        # def rInorder(root, res):
        #     if root is None:
        #         return

        #     rInorder(root.left, res)
        #     res.append(root.val)
        #     rInorder(root.right, res)

        #     return res

        # return inorder(root)