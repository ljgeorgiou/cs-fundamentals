from collections import deque

## Using deque
queue: deque[str] = deque()
queue.append("Steven")
queue.append("Bob")
queue.append("Julie")
queue.append("Robert")
queue.append("Frank")
while queue:
    print(f"Serving {queue.popleft()}")

## is_balanced Function using stack:
def is_balanced(text: str) -> bool:
    bracket_map: dict[str, str] = {"(" : ")", "[" : "]", "{" : "}"}
    stack: list[str] = []

    for char in text:
        if char in bracket_map:
            stack.append(char)
        elif not stack or bracket_map[stack.pop()] != char:
            return False
        
    return not stack

print(is_balanced("()"))        # True - single pair
print(is_balanced("{[()]}"))    # True - nested
print(is_balanced("([)]"))      # False - crossed brackets
print(is_balanced("("))         # False - unclosed opener
print(is_balanced(")"))         # False - closer with nothing to match
print(is_balanced(""))          # True - empty string is balanced