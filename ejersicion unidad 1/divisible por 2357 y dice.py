numero = int(input("Ingrese un número: "))

divisibles = []

if numero % 2 == 0:
    divisibles.append(2)
if numero % 3 == 0:
    divisibles.append(3)
if numero % 5 == 0:
    divisibles.append(5)
if numero % 7 == 0:
    divisibles.append(7)

if len(divisibles) > 0:
    print(numero, "es divisible por los siguientes números:", divisibles)
else:
    print(numero, "no es divisible por 2, 3, 5 ni 7.")
