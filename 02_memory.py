from typing import Any

a = [1, 2, 3]

def swap_first_last(items: list[Any]) -> None:
    items[0], items[-1] = items[-1], items[0]

swap_first_last(a) # swap the first and last item list a
print(a) # [3, 2, 1]

b = [4, 5, 6]

def swapped_copy(items: list[Any]) -> list[Any]:
    result = items.copy()
    result[0], result[-1] = result[-1], result[0]
    return result

c = swapped_copy(b) 
print(b) # [4, 5, 6]
print(c) # [6, 5, 4]