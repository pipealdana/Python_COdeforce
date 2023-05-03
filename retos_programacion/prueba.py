
def is_palindrome(s):
    return s == s[::-1]

def count_palindromes(s, x):
    seen_times = set()
    count = 0
    while s not in seen_times:
        seen_times.add(s)
        if is_palindrome(s):
            count += 1
        h, m = map(int, s.split(":"))
        m += x
        h += m // 60
        h %= 24
        m %= 60
        s = f"{h:02d}:{m:02d}"
    return count

t = int(input())
for _ in range(t):
    s, x = input().split()
    x = int(x)
    print(count_palindromes(s, x))