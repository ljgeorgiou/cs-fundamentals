import random
from ch11_searching_and_sorting import mergesort, binary_search

def test_sort_empty():
    assert mergesort([]) == []

def test_sort_one_item():
    assert mergesort([1]) == [1]

def test_sort_smallest_at_end():
    assert mergesort([5, 6, 7, 4]) == [4, 5, 6, 7]

def test_sort_already_sorted():
    assert mergesort([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_sort_reverse_sorted():
    assert mergesort([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_sort_odd_length():
    assert mergesort([3, 1, 2]) == [1, 2, 3]

def test_sort_with_duplicates():
    assert mergesort([5, 5, 7, 4]) == [4, 5, 5, 7]

def test_sort_random_lists():
    for _ in range(100):
        items = [random.randint(-50, 50) for _ in range(random.randint(0, 1000))]
        expected = sorted(items)
        assert mergesort(items) == expected

def test_search_empty():
    assert binary_search([], 3) is False

def test_search_one_item_found():
    assert binary_search([7], 7) is True

def test_search_one_item_missing():
    assert binary_search([7], 3) is False

def test_search_target_at_start():
    assert binary_search([1, 2, 3, 4], 1) is True

def test_search_target_at_end():
    assert binary_search([1, 2, 3, 4], 4) is True

def test_search_with_duplicates():
    assert binary_search([1, 2, 2, 2, 3], 2) is True

def test_search_missing_bigger_than_all():
    assert binary_search([1, 2, 3, 4], 5) is False

def test_search_missing_smaller_than_all():
    assert binary_search([1, 2, 3, 4], 0) is False

def test_search_missing_in_gap():
    assert binary_search([1, 3, 5, 7], 4) is False