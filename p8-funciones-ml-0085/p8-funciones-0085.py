# Ricardo lopez NC = 0085
print("ejemplo 1")
mensaje = "Aprendiendo Python"
longitud = len(mensaje)

print(longitud)
print("ejemplo 2")
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area
resultado = calcular_area_rectangulo(5, 3)
print(f"El área es: {resultado}")  
print("ejemplo 3")
def saludar_usuario(nombre):
    print(f"¡Hola, {nombre}! Bienvenido al curso.")


salida = saludar_usuario("Mariano")


print(salida)  
print("ejemplo 4")
def solicitar_edad():
   
    entrada = input("Ingresa tu edad: ")
    edad = int(entrada)
    
    if edad >= 18:
        return "Eres mayor de edad"
    else:
        return "Eres menor de edad"


estado = solicitar_edad()
print(estado)
print("ejemplo 5")
def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b


num1 = 10
num2 = 5

suma = sumar(num1, num2)
resultado_final = multiplicar(suma, 2)

print(f"El resultado final es: {resultado_final}")  
print("programa echo por Ricardo lopez NC = 0085")