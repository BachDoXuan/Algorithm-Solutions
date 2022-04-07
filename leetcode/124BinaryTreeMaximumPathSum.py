"""
A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the sequence has an edge connecting them. A node can only appear in the sequence at most once. Note that the path does not need to pass through the root.

The path sum of a path is the sum of the node's values in the path.

Given the root of a binary tree, return the maximum path sum of any non-empty path.

 

Example 1:


Input: root = [1,2,3]
Output: 6
Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 = 6.
Example 2:


Input: root = [-10,9,20,null,null,15,7]
Output: 42
Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 + 7 = 42.
 

Constraints:

The number of nodes in the tree is in the range [1, 3 * 104].
-1000 <= Node.val <= 1000
"""

from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeMaxima(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None

        if root.left is None and root.right is None:
            return [root.val, max(0, root.val)]
        elif root.left is None:
            rightMaxima = self.treeMaxima(root.right)
            return [max(rightMaxima[0], rightMaxima[1] + root.val, root.val),
                    max(root.val + rightMaxima[1], root.val, 0)]
        elif root.right is None:
            leftMaxima = self.treeMaxima(root.left)
            return [max(leftMaxima[0], leftMaxima[1] + root.val, root.val),
                    max(root.val + leftMaxima[1], root.val, 0)]
        else:
            leftMaxima = self.treeMaxima(root.left)
            rightMaxima = self.treeMaxima(root.right)
            return [max(leftMaxima[0], rightMaxima[0], 
                    root.val, root.val + leftMaxima[1], root.val + rightMaxima[1],
                    root.val + leftMaxima[1] + rightMaxima[1]), 
                    max(0, root.val + max(leftMaxima[1], rightMaxima[1]))]

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        return self.treeMaxima(root)[0]