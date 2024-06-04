from collections import deque


def is_palindrome(str):
    str = str.lower().replace(" ", "")
    queue = deque(str)
    while len(queue) > 1:
        if queue.popleft() != queue.pop():
            return False
    return True


print(is_palindrome("Я несу гусеня"))
print(is_palindrome("This is not palindrome"))
print(is_palindrome("Де помити мопед"))
print(is_palindrome("The quick brown fox jumps over the lazy dog"))
