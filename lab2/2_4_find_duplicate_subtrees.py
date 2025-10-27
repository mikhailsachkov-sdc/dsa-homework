# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        result = []
        tree_id = {} # maps (val, left_id, right_id) -> uid
        count = {} # maps id -> frequency
        uid = [1]

        stack = [(root, False)] # (node, visited)
        node_to_id = {} # node -> subtree id

        while stack:
            node, visited = stack.pop()
            if node is None:
                continue
            if visited:
                left_id = node_to_id.get(node.left, 0)
                right_id = node_to_id.get(node.right, 0)
                key = (node.val, left_id, right_id)
                if key not in tree_id:
                    tree_id[key] = uid[0]
                    uid[0] += 1
                nid = tree_id[key]
                node_to_id[node] = nid
                count[nid] = count.get(nid, 0) + 1
                if count[nid] == 2:
                    result.append(node)
            else:
                stack.append((node, True))
                stack.append((node.right, False))
                stack.append((node.left, False))

        return result

