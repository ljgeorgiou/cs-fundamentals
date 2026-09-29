def mergesort(items: list[int]) -> list[int]:
    if len(items) <= 1:
        return items
    middle = len(items) // 2
    left_side = mergesort(items[:middle])
    right_side = mergesort(items[middle:])
    return merge(left_side, right_side)

def merge(left: list[int], right: list[int]) -> list[int]:
    result: list[int] = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] <  right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j +=1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print(mergesort([]))                          # []
print(mergesort([7]))                         # [7]
print(mergesort([1, 2]))                      # [1, 2]
print(mergesort([2, 1]))                      # [1, 2]
print(mergesort([5, 2, 9]))                   # [2, 5, 9]
print(mergesort([5, 2, 9, 1]))                # [1, 2, 5, 9]
print(mergesort([1, 2, 3, 4, 5]))             # [1, 2, 3, 4, 5]
print(mergesort([5, 4, 3, 2, 1]))             # [1, 2, 3, 4, 5]
print(mergesort([3, 1, 3, 2, 1]))             # [1, 1, 2, 3, 3]
print(mergesort([4, 4, 4, 4]))                # [4, 4, 4, 4]
print(mergesort([-3, 0, -1, 5, -10]))         # [-10, -3, -1, 0, 5]
print(mergesort([1000, -1000, 0, 999, 1]))    # [-1000, 0, 1, 999, 1000]

print(merge([1, 4, 9], [2, 3, 10]))           # [1, 2, 3, 4, 9, 10]
print(merge([], [1, 2]))                      # [1, 2]
print(merge([1, 2], []))                      # [1, 2]
print(merge([1, 1], [1]))                     # [1, 1, 1]


def count_occurrences(sorted_items: list[int], target: int) -> int:
    
    def find_first() -> int:
        low_idx = 0
        high_idx = len(sorted_items) - 1
        first_idx = -1
        while low_idx <= high_idx:
            mid_idx = (low_idx + high_idx) // 2
            if sorted_items[mid_idx] == target:
                first_idx = mid_idx
                high_idx = mid_idx - 1
            elif sorted_items[mid_idx] < target:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx - 1
        return first_idx

    def find_last() -> int:
        low_idx = 0
        high_idx = len(sorted_items) - 1
        last_idx = -1
        while low_idx <= high_idx:
            mid_idx = (low_idx + high_idx) // 2
            if sorted_items[mid_idx] == target:
                last_idx = mid_idx
                low_idx = mid_idx + 1
            elif sorted_items[mid_idx] < target:
                low_idx = mid_idx + 1
            else:
                high_idx = mid_idx - 1
        return last_idx

    first_idx = find_first()
    if first_idx == -1:
        return 0
    else:
        last_idx = find_last()
        return (last_idx - first_idx) + 1

e = [1, 2, 2, 2, 2, 3, 5, 7, 7, 7, 8, 10, 11, 11, 11, 11, 11]

print(count_occurrences([], 5)) #0
print(count_occurrences(e, 1))  #1
print(count_occurrences(e, 2))  #4
print(count_occurrences(e, 3))  #1
print(count_occurrences(e, 7))  #3
print(count_occurrences(e, 11)) #5
print(count_occurrences(e, 12)) #0