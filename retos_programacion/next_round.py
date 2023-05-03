#  auhtor: coyot2022
#  created: 18/04/23 16:38:37
#  complexity: O()
n, k = list(map(int, input().split()))
p = list(map(int, input().split()))
count=0
R = p[k-1]
for num in p:
    if num!=0 and num>=R:
        count+=1

print(count)