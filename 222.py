"""
完全二叉树的节点个数
BFS
中等
python 中没有null；用None来代替
"""
def countNodes(self, root: TreeNode) -> int:
        if root == None:
            return 0
        left=self.countNodes(root.left)
        right=self.countNodes(root.right)

        return left+right+1