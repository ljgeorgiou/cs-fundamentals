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