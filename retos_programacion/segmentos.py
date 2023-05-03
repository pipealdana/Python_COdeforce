tc= int(input())
while tc >0:
    ans= ""
    n= int(input())
    test= n/2
    while (test)>0:    
        ans+= "1"
        n-=1
    if n%2==0:
        ans[0]="7"
    print (ans)
    tc -=1
    break
