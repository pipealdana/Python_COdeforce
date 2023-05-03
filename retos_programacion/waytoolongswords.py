n = int(input())
pp = True
while n > 0:
    s = input("")
    t = len(s)
    if t>10:
        print(s[0],(t-2),s[t-1],sep='')
    else:
        print(s)
    n -= 1
