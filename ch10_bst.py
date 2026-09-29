class Node:
    def __init__(self, value: int) -> None:
        self.value: int = value
        self.left: Node | None = None
        self.right: Node | None = None

    def find_max(self) -> int | float:
        def helper(item: Node | None, biggestSoFar: int) -> int | float:
            if item is None:
                return float("-inf")
            left_biggest = helper(item.left, item.value)
            right_biggest = helper(item.right, item.value)
            biggest = max(left_biggest, right_biggest)
            if item.value > biggest:
                return item.value
            else:
                return biggest
        return helper(self, self.value)

    def count(self) -> int:
        def helper(item: Node | None) -> int:
            if item is None:
                return 0
            else:
                return 1 + helper(item.left) + helper(item.right)
        return helper(self)

    def count_leaves(self) -> int:
        def helper(item: Node | None) -> int:
            if item is None:
                return 0
            left_side = helper(item.left)
            right_side = helper(item.right)
            if left_side == 0 and right_side == 0:
                return 1
            return left_side + right_side
        return helper(self)

    def total(self) -> int:
        def helper(item: Node | None) -> int:
            if item is None:
                return 0
            else:
                return item.value + helper(item.left) + helper(item.right)
        return helper(self)

    def height(self) -> int:
        def helper(item: Node | None) -> int:
            if item is None:
                return 0
            left_height = helper(item.left)
            right_height = helper(item.right)
            max_height = 0
            if left_height > right_height:
                max_height = left_height
            else:
                max_height = right_height
            return 1 + max_height
        return helper(self)

    def in_order(self) -> list[int]:
        vals: list[int] = []
        def helper(item: Node | None) -> None:
            if item is None:
                return
            helper(item.left)
            vals.append(item.value)
            helper(item.right)
        helper(self)
        return vals

    def mirror(self) -> None:
        def helper(item: Node | None) -> Node | None:
            if item is None:
                return None
            switch_left_nodes = helper(item.left)
            switch_right_nodes = helper(item.right)
            item.left, item.right = switch_right_nodes, switch_left_nodes
            return item
        helper(self)

    def __repr__(self) -> str:
        left_str = f"{self.value}L{self.left}" if self.left else ""
        right_str = f"{self.value}R{self.right}" if self.right else ""
        return f"({self.value}[{left_str}{right_str}])"

class BST:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        def helper(item: Node, value: int) -> None:
            if value < item.value:
                if item.left is None:
                    item.left = Node(value)
                    return
                helper(item.left, value)
            elif value > item.value:
                if item.right is None:
                    item.right = Node(value)
                    return
                helper(item.right, value)
            else:
                raise ValueError(f"Sorryy mate, already got one of these {value}")
        if self.root is None:
            self.root = Node(value)
        else:
            helper(self.root, value)
        
    def in_order(self) -> list[int]:
        vals: list[int] = []
        def helper(item: Node | None) -> None:
            if item is None:
                return
            helper(item.left)
            vals.append(item.value)
            helper(item.right)
        helper(self.root)
        return vals

    def find_max(self) -> int:
        if self.root is None:
            raise ValueError("Sorry mate, doesn't exist here")
        current = self.root
        while current.right is not None:
            current = current.right
        return current.value

    def find_min(self) -> int:
        if self.root is None:
            raise ValueError("Sorry mate, doesn't exist here")
        current = self.root
        while current.left is not None:
            current = current.left
        return current.value
        
            

    def delete(self, value: int) -> Node | None:
        def helper(item: Node | None, value: int) -> tuple[Node | None, Node | None]:
            if item is None:
                return None, None
            elif value < item.value:
                deleted, item.left = helper(item.left, value)
                return deleted, item
            elif value > item.value:
                deleted, item.right = helper(item.right, value)
                return deleted, item
            elif item.left is None:
                return item, item.right
            elif item.right is None:
                return item, item.left
            elif item.right.left is None:
                item.right.left = item.left
                return item, item.right
            else:
                pre, cur = item.right, item.right.left
                while cur.left:
                    pre, cur = cur, cur.left
                pre.left, cur.left, cur.right = cur.right, item.left, item.right
                return item, cur

        deleted, self.root = helper(self.root, value)
        if deleted:
            deleted.left, deleted.right = None, None
        return deleted

    def __repr__(self) -> str:
        return str(bst.in_order())


bst: BST = BST()
bst.insert(8)
bst.insert(3)
bst.insert(11)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(9)
print(bst.root)
deleted = bst.delete(8)
print(deleted)
print(bst)
print(bst.root)