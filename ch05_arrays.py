from typing import Any
import time

a: list[Any] = []
for i in range(25_000):
    a.append(i)
    a.append(43)

def remove_all_v1(items: list[int], value: int) -> list[int]:
    while value in items:
        items.remove(value)
    return items

b: list[Any] = []
for i in range(25_000):
    b.append(i)
    b.append(43)

def remove_all_v2(items: list[int], value: int) -> list[int]:
    return [item for item in items if item != value]

## V1 Test:
start_time: float = time.time()
remove_all_v1(a, 43)
end_time: float = time.time()
print(end_time - start_time) # 3.420 seconds

## V2 Test:
start_time: float = time.time()
remove_all_v2(b, 43)
end_time: float = time.time()
print(end_time - start_time) # 0.001 seconds

# The big-O of remove_all_v1 is O(n^2) because when it removes that value it needs to reshuffle the entire list (O(n)),
# and worst case, it does this n times - n * n is n^2. The big-O of remove_all_v2 is O(n) because this doesn't need to
# reshuffle the list at all, it just rebuilds a new list. Worst case, none of the items is the value and therefore it
# rebuilds the entire list - O(n). Therefore, I would use remove_all_v2.