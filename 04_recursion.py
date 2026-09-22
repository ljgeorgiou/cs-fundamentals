from typing import Any

## Recurisve power function
def power(base: int, exp: int) -> int:
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

print(power(2, 5)) #32

## Add digits of a number using recursion
def sum_digits(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n%10 + sum_digits(n//10)

print(sum_digits(1234)) #10
print(sum_digits(548)) #17

## Recursive is_palindrome
def is_palindrome(s: str) -> bool:
    def helper(s: str) -> str:
        if len(s) == 0:
            return ""
        else:
            return s[-1] + helper(s[0:-1])
    s_backwards: str = helper(s)
    return s_backwards == s

print(is_palindrome("racecar")) #True
print(is_palindrome("abc")) #False

## Recursive max_depth
def max_depth(data: list[Any]) -> int:
    deepest = 1                         
    for item in data:
        if isinstance(item, list):      
            depth_here = 1 + max_depth(item)   
            if depth_here > deepest:
                deepest = depth_here    
    return deepest

print(max_depth([1, [1, [2, 3]]])) #3
print(max_depth([1, 2])) #1

## Flatten a list
def flatten(data: list[Any]) -> list[Any]:
    new_list: list[Any] = []
    for item in data:
        if isinstance(item, list):
            new_list += flatten(item)
        else:
            new_list.append(item)
    return new_list

print(flatten([1, [2, 3, [4, 5]]])) # [1, 2, 3, 4, 5]
print(flatten([1, 2, 3, 4])) # [1, 2, 3, 4]
print(flatten([])) # []