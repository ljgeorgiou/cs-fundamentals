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

root = Node(8)
root.left = Node(3)
root.right = Node(10)

root.left.left = Node(1)
root.left.right = Node(6)

root.right.right = Node(14)

print(root.count())        # 6
print(root.count_leaves()) #3
print(root.total())        # 42
print(root.height())       # 3
print(root.in_order())     # [1, 3, 6, 8, 10, 14]
print(root.find_max())     # 14
root.mirror()   
print(root.in_order())     # [14, 10, 8, 6, 3, 1]