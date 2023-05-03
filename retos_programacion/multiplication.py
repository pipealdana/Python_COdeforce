#Complejidad O(n)
n, x = map(int, input().split())
count = 0

for i in range(1, n + 1):
    if x % i == 0:
        if x//i * i ==x and x//i <=n:
            count += 1

print(count)

#Lo que hace el operador // es darme el entero
#resultante de una division

"""Primero: La i recorre los numeros de 1 hasta n+1.
    Despues de ello revisa si ese numero es multiplo de x,
    si es asi, en la variable c, se guardara el valor de la division
    entera de x entre i.
    Si el cociente de esa division es menor o igual a n, entonces le sumara 1 
    al contador
"""



