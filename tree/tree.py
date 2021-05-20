from node import TreeNode

class Tree:

    def __init__(self) -> None:
        self.root: TreeNode = None
        self.count: int = 0

    def length(self) -> int:
        return self.count

    def put(self, key = None):
        if key is None:
            return
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._put(self.root, key)
    
    def _put(self, node: TreeNode = None, key  = None):
        if node.key == key:
            return
        elif key > node.key:
            if not node.has_right_child():
                node.right = TreeNode(key, node)
                self.count += 1
            else:
                self._put(node.get_right_child(), key)
        else:
            if not node.has_left_child():
                node.left = TreeNode(key, node)
                self.count += 1
            else:
                self._put(node.get_left_child(), key)

    def get(self, key = None) -> TreeNode:
        if key is None:
            return
        if self.root is None:
            return None
        if self.root.key == key:
            return self.root
        else:
            return self._get(self.root, key)

    def _get(self, node: TreeNode = None, key = None) -> TreeNode:
        if node.key == key:
            return node
        elif key > node.key:
            if node.has_right_child():
                return self._get(node.get_right_child(), key)
            else:
                return None
        else:
            if node.has_left_child():
                return self._get(node.get_left_child(), key) 
            else:
                return None

    def get_it(self, key = None) -> TreeNode:
        if key is None:
            return None
        node: TreeNode = self.root
        found: bool = False
        while node is not None and not found:
            if node.key == key:
                found = True
            elif key > node.key:
                node = node.get_right_child()
            else:
                node = node.get_left_child()

        if not found:
            return None
        return node


    def contains(self, key = None):
        if key is None:
            return False
        node: TreeNode = self.root
        found: bool = False
        while node is not None and not found: 
            if node.key == key:
                found = True
            elif key > node.key:
                node = node.get_right_child()
            else:
                node = node.get_left_child()

        return found

    def delete(self, key = None):
        node_to_delete: TreeNode = self.get(key)
        if node_to_delete is None:
            return
        if node_to_delete == self.root:
            if node_to_delete.is_leaf():
                self.root = None
                self.count -= 1
            elif node_to_delete.has_both_children():
                tmp: TreeNode = node_to_delete.get_left_child().get_max()
                tmp_key = tmp.key
                self.delete(tmp_key)
                node_to_delete.key = key
            elif node_to_delete.has_left_child():
                self.root = node_to_delete.get_left_child()
                self.count -= 1
            else:
                self.root = node_to_delete.get_right_child()
                self.count -= 1
            self.root.parent = None
        else:
            if node_to_delete.is_leaf():
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
                self.count -= 1
            elif node_to_delete.has_both_children():
                tmp: TreeNode = node_to_delete.get_left_child().get_max()
                tmp_key = tmp.key
                self.delete(tmp_key)
                node_to_delete.key = key
            elif node_to_delete.has_left_child():
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.get_left_child()
                else:
                    node_to_delete.parent.right = node_to_delete.get_left_child()
                node_to_delete.get_left_child().parent = node_to_delete.parent
                self.count -= 1
            else:
                if node_to_delete.is_left_child():
                    node_to_delete.parent.left = node_to_delete.get_right_child()
                else:
                    node_to_delete.parent.right = node_to_delete.get_right_child()
                node_to_delete.get_right_child().parent = node_to_delete.parent
                self.count -= 1

    def get_min(self) -> 'TreeNode':
        if self.root is None:
            return None
        node: 'TreeNode' = self.root
        while node.get_left_child() is not None:
            node = node.get_left_child()
        return node

    def get_max(self) -> 'TreeNode':
        if self.root is None:
            return None
        node: 'TreeNode' = self.root
        while node.get_right_child() is not None:
            node = node.get_right_child()
        return node

    
