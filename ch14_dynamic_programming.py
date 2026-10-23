def fib(n: int) -> int:
    if n < 2:
        return n
    table = [0] * (n+1)
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(fib(50)) # 12586269025

def ways(n: int) -> int:
    table = [1] * (n+1)
    if n >= 2:
        table[2] = 2
    for i in range(3, n+1):
        table[i] = table[i-1] + table[i-2] + table[i-3]
    return table[n]

print(ways(4)) # 7

def min_coins(coins: list[int], amount: int) -> int:
    table = [float("inf")] * (amount + 1)
    table[0] = 0
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and table[a-c] + 1 < table[a]:
                table[a] = table[a-c] + 1
    if table[amount] == float("inf"):
        return -1
    return table[amount]

print(min_coins([1, 3, 4], 6)) # 2
print(min_coins([2], 3)) # -1

def count_ways_coins(coins: list[int], amount: int) -> int:
    table = [0] * (amount + 1)
    table[0] = 1
    for c in coins:
        for a in range(c, amount + 1):
            table[a] = table[a] + table[a-c]
    return table[amount]

print(count_ways_coins([1, 2, 5], 5)) # 4