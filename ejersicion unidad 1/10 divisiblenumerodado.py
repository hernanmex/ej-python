numero = int(input("Ingrese un número: "))

print("Los divisores de", numero, "son:")

for divisor in range(1, numero + 1):
    if numero % divisor == 0:
        print(divisor)
