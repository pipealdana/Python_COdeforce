#Complejidad O(1)
n = int(input())
while True:
    p = list(map(int, input().split()))
    if len(p) == n:
        aux = [(num/n) for num in p]
        ans= (sum(aux))
        print("{:.12f}".format(ans))
        break
    else:
        break
