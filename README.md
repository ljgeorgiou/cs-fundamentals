# cs-fundamentals

My work as I learn computer science fundamentals, data structures, algorithms, and Big O, building each concept from scratch in Python to understand how it really works.

This is Phase 2 of my self-study path towards becoming an AI engineer.

## What's in here

Each file covers one topic:

- `ch02_memory.py` - references, aliasing, and copying
- `ch03_big_o.py` - measuring efficiency, and list vs set lookup speed
- `ch04_recursion.py` - recursion, base cases, and the call stack
- `ch05_arrays.py` - how a Python list works underneath, and why some list operations are fast and others are slow
- `ch06_linked_lists.py` - a linked list built from scratch, with a tail so adding to the end is O(1)
- `ch07_stacks_queues.py` - stacks and queues, and when to use each one
- `ch08_hash_map.py` - a hash map built from scratch, with buckets and resizing
- `ch09_trees_and_traversals.py` - binary trees, and the three ways to walk through one (in-order, pre-order and post-order)
- `ch10_bst.py` - a binary search tree, with insert, search, min, max, size, height and delete
- `ch11_searching_and_sorting.py` - binary search, merge sort, and counting a value in a sorted list using two binary searches
- `ch12_graphs_bfs_dfs.py` - a graph class with BFS, DFS, shortest path, directed edges and cycle detection
- `ch13_heaps_and_dijkstra.py` - heaps with `heapq`, finding the k smallest items, and Dijkstra's algorithm for the shortest weighted path
- `ch14_dynamic_programming.py` - dynamic programming: Fibonacci, climbing stairs, the fewest coins to make an amount, and counting coin combinations
- `test_linked_list.py` - pytest tests for my linked list
- `test_with_pytest.py` - pytest tests for my binary search and merge sort


## Running the code

You need Python 3.10 or newer.

Set up a virtual environment and install pytest:

```
python -m venv .venv
source .venv/Scripts/activate     # Windows (Git Bash)
source .venv/bin/activate         # Mac / Linux
pip install pytest
```

Each file runs on its own, for example:

```
python ch06_linked_lists.py
```

Run all the tests from the main cs-fundamentals folder:

```
pytest
```

## Final project

The final project for this phase is in its own repo: [data-structures-from-scratch](https://github.com/ljgeorgiou/data-structures-from-scratch). It has a hash map, a binary search tree and a graph built from scratch with full pytest tests, plus a route finder for UK towns that uses BFS and Dijkstra.

## Blog posts

- [Big-O explained simply](https://dev.to/ljgeorgiou/big-o-explained-simply-4888)
- [BFS vs DFS explained with one small graph](https://dev.to/ljgeorgiou/bfs-vs-dfs-explained-with-one-small-graph-3dj4)