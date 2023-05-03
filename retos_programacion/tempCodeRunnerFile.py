t = int(input())
n = list(map(int,(input())))
ans = 0

while t>0:
    for num in n:
        if n & (n-1) == 0: # Es una potencia de 2
            ans -= n
        else: # No es una potencia de 2
            ans += n
    t-=1
print(ans)