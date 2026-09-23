from typing import Any

class Node:
    def __init__(self, value: Any) -> None:
        self.value: Any = value
        self.next: Any = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def __len__(self) -> int:
            total: int = 0
            if self.head is None:
                return total
            current = self.head
            while current is not None:
                total += 1
                current = current.next
            return total

    def prepend(self, value: Any) -> None:
        node: Node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head = node
            
    def append(self, value: Any) -> None:
        node: Node = Node(value)
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def delete(self, value: Any) -> bool:
        if self.head is None:
            return False
        elif self.head.value == value:
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return True
        else:
            current = self.head
            while current.next is not None:
                if current.next.value == value:
                    current.next = current.next.next
                    if current.next is None:
                        self.tail = current
                    return True
                current = current.next
            return False

    def find(self, value: Any) -> bool:
        if self.head is None:
            return False
        else:
            current = self.head
            while current is not None:
                if current.value == value:
                    return True
                current = current.next
            return False

    def to_list(self) -> list[Any]:
        new_list: list[Any] = []
        current = self.head
        while current is not None:
            new_list.append(current.value)
            current = current.next
        return new_list

linked_list = LinkedList()

## Using prepend
linked_list.prepend(3)
print(linked_list.tail.value) #3
linked_list.prepend(5)
print(linked_list.tail.value) # 3
linked_list.prepend(7)
print(linked_list.to_list()) # [7, 5, 3]
print(linked_list.tail.value) #3

## Using append
linked_list.append(5)
print(linked_list.tail.value) #5
linked_list.append(7)
linked_list.append(9)
print(linked_list.to_list()) # [7, 5, 3, 5, 7, 9]
print(linked_list.tail.value) #9

## Using find
print(linked_list.find(3)) #True
print(linked_list.find(5)) #True
print(linked_list.find(7)) #True
print(linked_list.find(9)) #True
print(linked_list.find(11)) #False
print(linked_list.find(13)) #False
print(linked_list.find(15)) #False

## Using len
print(len(linked_list)) #6

## Using delete
new_linked_list: LinkedList = LinkedList()
new_linked_list.prepend(2)
new_linked_list.prepend(4)
new_linked_list.prepend(6)
print(new_linked_list.tail.value) #2
print(new_linked_list.to_list())  # [6, 4, 2]
print(new_linked_list.delete(6))  # True
print(new_linked_list.to_list())  # [4, 2]
print(new_linked_list.delete(4))  # True
print(new_linked_list.to_list())  # [2]
print(new_linked_list.delete(2))  # True
print(new_linked_list.to_list())  # []
print(new_linked_list.tail)       # None
print(new_linked_list.delete(5))  # False

new_linked_list.append(5)
new_linked_list.append(7)
new_linked_list.append(9)
print(new_linked_list.to_list()) # [5, 7, 9]
print(new_linked_list.delete(99))# False
print(new_linked_list.delete(7)) # True
print(new_linked_list.to_list()) # [5, 9]
print(new_linked_list.delete(9)) # True
print(new_linked_list.to_list()) # [5]
new_linked_list.append(9)        
print(new_linked_list.to_list()) # [5, 9]
print(new_linked_list.delete(5)) # True
print(new_linked_list.to_list()) # [9]

empty_list: LinkedList = LinkedList()
print(empty_list.delete(1)) # False