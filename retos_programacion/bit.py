#  auhtor: coyot2022
#  created: 19/04/23 14:14:44
#  complexity: O(n)
n= int(input())
x=0
while n>0:
    bit=input("")
    if bit=="++X" or bit=="X++":
        x+=1
    elif bit=="--X" or bit=="X--":
        x-=1

    n-=1
print (x)