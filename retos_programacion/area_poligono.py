def poligono():
    entrada=(float(input("Que desea calcular: 1. Triangulo, 2. Cuadrado, 3. Rectangulo:  ")))
    if entrada==1:
        base=(float(input("Ingrese la base del triangulo: ")))
        altura=(float(input("Ingrese la altura del triangulo: ")))
        area= (base*altura)/2
        print ("El area del triangulo es: ", area)
    if entrada==2:
        base=(float(input("Ingrese la longitud de uno de los lados: ")))
        area= (base*base)
        print("El area del cuadrado es: ", area)
    if entrada==3:
        base=(float(input("Ingrese la base del rectangulo: ")))
        altura=(float(input("Ingrese la altura del rectangulo: ")))
        area=(base*altura)  
        print("El area del rectangulo es: ", area)      

if __name__ == "__main__":
    poligono() 
