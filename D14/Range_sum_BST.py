# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        result = 0 
        stack = [root]
        while(stack):
            singleNode = stack.pop()
            if(singleNode):
                if(singleNode.val<=R and singleNode.val>=L):
                    result = result+singleNode.val
                if L < singleNode.val:
                    stack.append(singleNode.left)
                if singleNode.val < R:
                    stack.append(singleNode.right)
        return result