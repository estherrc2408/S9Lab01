import unittest
def sumar(a, b):
    if type(a) != int or type(b) != int:
        return "Ambos deben ser números enteros"
    return a + b

def restar(a, b):
    if type(a) != int or type(b) != int:
        return "Ambos deben ser números enteros"
    return a - b

def multiplicar(a, b):
    if type(a) != int or type(b) != int:
        return "Ambos deben ser números enteros"
    return a * b

def dividir(a, b):
    if type(a) != int or type(b) != int:
        return "Ambos deben ser números enteros"
    if b != 0:
        return a / b
    else:
        raise ZeroDivisionError("Error: No se puede dividir por cero")

# Aquí puedes agregar más funciones según sea necesario
if __name__ == "__main__":
    print(sumar(5, 3))
    print(restar(8, 3))
    print(multiplicar(4, 6))
    print(dividir(10, 2))
    print(dividir(7, 0))  # Esto debería imprimir el mensaje de error

