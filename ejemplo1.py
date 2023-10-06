#ejemplo 1
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("No se puede dividir entre 0")

#ejemplo 2
try:
    valor = int(input("Ingrese un número: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debe ingresar un número válido")
except ZeroDivisionError:
    print("Error: No puedes dividir por 0")

#ejemplo 3
try:
    valor = int(input("Ingrese un número: "))
    resultado = 10 / valor
except ValueError:
    print("Error: Debe ingresar un número válido")
except ZeroDivisionError:
    print("Error: No puedes dividir por 0")
else:
    print(f"El resultado es {resultado}")


try:
    a = int(input("Digite el primer numero: "))
    b = int(input("Digite el segundo numero: "))
except ZeroDivisionError:
    print("Error: División por cero no permitida.")
else:
    print("El resultado es:", resultado)
finally:
    print("Operación finalizada.")

#ejemplo 4
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
except FileNotFoundError:
    print("Error: El archivo no existe.")
finally:
    archivo.close()


def dividir(a, b):
    if b == 0:
        raise ValueError("No puedes dividir entre 0")
    return a / b

try:
    resultado = dividir(10, 0)
except ValueError as e:
    print(e)
else:
    print(resultado)