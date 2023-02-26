
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        ans = []
        def preorderHelper(root, ans):
            if root == None:
                return ans
            ans.append(root.val)
            for child in root.children:
                preorderHelper(child, ans)
                     
        preorderHelper(root, ans)
        return ans