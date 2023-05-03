#  auhtor: coyot2022
#  created: 18/04/23 16:12:10
#  complexity: O(n*p)
count=0
n=int(input())
while n>0:
    p = list(map(int, input().split()))
    aux=0
    for i in range (0, len(p)):
        if p[i]==1:
            aux+=1
    if aux>=2:
        count+=1
    n-=1
print (count)

