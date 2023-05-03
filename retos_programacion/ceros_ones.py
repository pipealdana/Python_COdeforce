#Complejidad O(n)
n = int(input())
p = input()

count = 0
aux = 0
if len(p)==n:
    for char in p:
        if char == "0":
            count += 1
        elif char == "1":
            aux += 1


ans = abs(count - aux) #La funcion abs me devuelve el valor absoluto
                        #De una resta
print(ans)

            



