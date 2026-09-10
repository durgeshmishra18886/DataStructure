# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        count_matching = 0

        def post_order(node):
            nonlocal count_matching
            if not node:
                return 0, 0  # (sum, count)

            # Recurse on children
            left_sum, left_count = post_order(node.left)
            right_sum, right_count = post_order(node.right)

            # Compute current subtree values
            total_sum = left_sum + right_sum + node.val
            total_count = left_count + right_count + 1

            # Check condition (integer division handles floor)
            if node.val == total_sum // total_count:
                count_matching += 1

            return total_sum, total_count

        post_order(root)
        return count_matching
        