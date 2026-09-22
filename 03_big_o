import time
from typing import Any

# Using a list
def has_duplicates_v1(items: list[Any]) -> bool:
    already_seen: list[Any] = []
    for i in items:
        if i not in already_seen:
            already_seen.append(i)
        else:
            return True
    return False

# Using a set
def has_duplicates_v2(items: list[Any]) -> bool:
    already_seen: set[Any] = set()
    for i in items:
        if i not in already_seen:
            already_seen.add(i)
        else:
            return True
    return False

# Creating a list of 20,000 items:
a: list[int] = []
for i in range(20000):
    a.append(i)

# Testing time for v1
start = time.time()
has_duplicates_v1(a)
end = time.time()
print(end - start) # 1.117 seconds

# Testing time for v2
start = time.time()
has_duplicates_v2(a)
end = time.time()
print(end - start) # 0.001 seconds

# Version two is quicker because it checks membership against a set instead of a list.
# Checking if something is in a set has constant lookup time - O(1) - whereas checking
# if something is in a list has linear lookup time - O(n).