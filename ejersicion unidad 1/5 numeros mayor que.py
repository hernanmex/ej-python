numero1 = int(input("Ingrese un numero: "))
numero2 = int(input("Ingrese otro numero: "))
numero3 = int(input("Ingrese otro numero: "))

if numero1 > numero2 and numero1 > numero3:
    print("el numero: " ,numero1 , " es mayor que :" , numero2, " y mayor que numero :", numero3,)
elif numero2 > numero1 and numero2 > numero3:
    print("el numero: " ,numero2 , " es mayor que :" , numero1, " y mayor que numero :" ,numero3,)
elif numero3 > numero1 and numero3 > numero2:
    print("el numero: " ,numero3 , " es mayor que :" , numero1 ," y mayor que numero :",numero2,)
else:
    print("todos números son iguales")
    
    
