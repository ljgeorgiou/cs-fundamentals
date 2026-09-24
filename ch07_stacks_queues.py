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


GREEN = "\033[0;32m"
RED = "\033[0;31m"
CLEAR = "\033[0;m"

def main():
    test_cases = [
        # --- Basic valid cases ---
        ("", True),              # empty string is balanced (nothing to match)
        ("()", True),            # single pair
        ("[]", True),
        ("{}", True),

        # --- Nested (tests reverse-order closing) ---
        ("([])", True),          # nested different types
        ("{[()]}", True),        # deeply nested
        ("(((())))", True),      # deeply nested same type

        # --- Sequential (multiple pairs in a row) ---
        ("()()", True),          # two pairs side by side
        ("()[]{}", True),        # three different pairs in sequence
        ("([]){}", True),        # mix of nested and sequential

        # --- Wrong order / crossed brackets (the classic failure) ---
        ("([)]", False),         # crossed — opens (,[  closes ),]
        ("{[}]", False),         # crossed different types
        (")(", False),           # closer before its opener

        # --- Unclosed openers (stack not empty at end) ---
        ("(", False),            # single unclosed opener
        ("((", False),           # two unclosed
        ("([]", False),          # one closes, one left open
        ("{[()]", False),        # everything nested but outer never closes

        # --- Unmatched closers (empty stack when a closer arrives) ---
        (")", False),            # single closer, nothing opened — MUST NOT crash
        ("())", False),          # extra closer at the end
        ("()]", False),          # wrong extra closer
        ("(]", False),           # opener then wrong closer

        # --- Mismatched pair ---
        ("(}", False),           # ( expects ) but got }
        ("[)", False),           # [ expects ] but got )

        # --- Longer realistic-ish cases ---
        ("((()))[]{}", True),    # long but valid
        ("((())", False),        # long, one unclosed
        ("{[()()]}[]", True),    # complex valid
        ("{[(])}", False),       # complex crossed
    ]

    correct = 0
    for given, expected in test_cases:
        actual = is_balanced(given)
        correct += int(expected == actual)
        colour = GREEN if actual == expected else RED
        print(f"{colour}{given=}, {expected=}, {actual=}{CLEAR}")
        
    print("----------------------")
    print(f"Score: {correct}/{len(test_cases)}")


if __name__ == "__main__":
    main()