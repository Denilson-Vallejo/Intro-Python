def cuadrado(a:float):
    return a*a

def triangulo(a:float, b:float):
    return (a*b)/2

def circulo(r:float):
    return 3.141592 * (r*r)

num= float(input("Ingrese un valor para el cuadrado:" ))
print("El área del cuadrado es: " + str(cuadrado(num)))

num2= float(input("Ingrese la altura del triángulo: "))
num= float(input("Ingrese la base del triángulo: "))
print("El área del triángulo es: " + str(triangulo(num, num2)))

num= float(input("Ingrese el radio del círculo: "))
print("El área del círculo es: " + str(circulo(num)))