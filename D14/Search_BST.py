# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        if(root is not None and root.val==val):
            return root
        if(root):
            if(root.val>val):
                return self.searchBST(root.left,val)

            elif(root.val<val):
                return self.searchBST(root.right,val)
        
        return
        