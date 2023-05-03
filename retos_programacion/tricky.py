n = int(input())
ans = 0

while n>0:    
   if n & (n-1) == 0: # Es una potencia de 2
      ans -= n
   else: # No es una potencia de 2
      ans += n
   n-=1 

print(ans)
#COmp