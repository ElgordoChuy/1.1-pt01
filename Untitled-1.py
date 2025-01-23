def menu():
    print("Seleccione una opción:")
    print("1. Suma de 'n' números (positivos y negativos)")
    print("2. Producto entre 'n' números")
    print("3. División entre 2 números")
    print("4. Calcular el factorial (n!)")
    print("5. Tablas de multiplicar (del 1 al 10)")
    print("6. Calcular el cuadrado y cubo de un número")
    print("7. Determinación del promedio de una serie de números")
    print("8. Aceptar 'n' números enteros e imprimir máximo, mínimo y total")
    print("9. Salir")

def suma_numeros():
    numeros = list(map(int, input("Ingrese los números separados por espacio: ").split()))
    print("La suma es:", sum(numeros))

def producto_numeros():
    numeros = list(map(int, input("Ingrese los números separados por espacio: ").split()))
    producto = 1
    for num in numeros:
        producto *= num
    print("El producto es:", producto)

def division_numeros():
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))
    if num2 != 0:
        print("La división es:", num1 / num2)
    else:
        print("Error: No se puede dividir entre cero.")

def factorial():
    n = int(input("Ingrese un número para calcular su factorial: "))
    if n < 0:
        print("Error: El factorial no está definido para números negativos.")
    else:
        resultado = 1
        for i in range(1, n + 1):
            resultado *= i
        print(f"El factorial de {n} es: {resultado}")

def tabla_multiplicar():
    n = int(input("Ingrese el número de la tabla (1-10): "))
    if 1 <= n <= 10:
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
    else:
        print("Error: Debe ingresar un número entre 1 y 10.")

def cuadrado_cubo():
    n = int(input("Ingrese un número: "))
    print(f"El cuadrado de {n} es: {n ** 2}")
    print(f"El cubo de {n} es: {n ** 3}")

def promedio():
    suma = 0
    contador = 0
    while True:
        valor = float(input("Ingrese un número (-1 para terminar): "))
        if valor == -1:
            break
        suma += valor
        contador += 1
    if contador > 0:
        print("El promedio es:", suma / contador)
    else:
        print("No se ingresaron números para calcular el promedio.")

def max_min_total():
    numeros = []
    while True:
        valor = int(input("Ingrese un número entero (-1 para terminar): "))
        if valor == -1:
            break
        numeros.append(valor)
    
    if numeros:
        print("Máximo:", max(numeros))
        print("Mínimo:", min(numeros))
        print("Total de valores:", len(numeros))
    else:
        print("No se ingresaron números.")

def main():
    while True:
        menu()
        opcion = input("Ingrese su opción: ")
        if opcion == '1':
            suma_numeros()
        elif opcion == '2':
            producto_numeros()
        elif opcion == '3':
            division_numeros()
        elif opcion == '4':
            factorial()
        elif opcion == '5':
            tabla_multiplicar()
        elif opcion == '6':
            cuadrado_cubo()
        elif opcion == '7':
            promedio()
        elif opcion == '8':
            max_min_total()
        elif opcion == '9':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()