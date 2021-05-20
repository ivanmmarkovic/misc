class TreeNode:

    def __init__(self, key = None, parent: 'TreeNode' = None, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.key = key
        self.parent: 'TreeNode' = parent
        self.left: 'TreeNode' = left
        self.right: 'TreeNode' = right

    def is_left_child(self) -> bool:
        return self.parent.get_left_child() == self

    def is_right_child(self) -> bool:
        return self.parent.get_right_child() == self

    def has_left_child(self) -> bool:
        return self.left is not None

    def has_right_child(self) -> bool:
        return self.right is not None

    def has_both_children(self) -> bool:
        return self.has_left_child() and self.has_right_child()

    def is_leaf(self) -> bool:
        return not self.has_left_child() and not self.has_right_child()

    def get_left_child(self) -> 'TreeNode':
        return self.left

    def get_right_child(self) -> 'TreeNode':
        return self.right

    def get_min(self) -> 'TreeNode':
        if self is None:
            return None
        node: 'TreeNode' = self
        while node.get_left_child() is not None:
            node = node.get_left_child()
        return node

    def get_max(self) -> 'TreeNode':
        if self is None:
            return None
        node: 'TreeNode' = self
        while node.get_right_child() is not None:
            node = node.get_right_child()
        return node