numero = int(input("Ingrese un numero: "))
if numero % 2 == 0:
    print("El número", numero, "es divisible por 2.")
elif numero % 3 == 0:
    print("El número", numero, "es divisible por 3.")
elif numero % 5 == 0:
    print("El número", numero, "es divisible por 5.")
elif numero % 7 == 0:
    print("El número", numero, "es divisible por 7.")
else:
    print("El número", numero, "no es divisible por 2, 3, 5 ni 7.")