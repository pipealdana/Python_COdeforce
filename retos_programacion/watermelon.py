import sys
input = sys.stdin.readline
output = sys.stdout.write

w = int(input())
if w%2==0 and w!=2:
    output("YES")
else:
    output("NO")