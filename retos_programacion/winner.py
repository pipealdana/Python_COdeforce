t=int(input())
name=str
score=int
name, score= map(input().split)

while t >0:
    if sorted(name)== name:
        ans= sum(score)
        print (ans, score)
    elif score > ans:
        print (name, score)
        
    t-1

