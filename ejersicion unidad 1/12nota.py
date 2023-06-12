nota = float(input("Ingrese la nota: "))

if nota >= 0 and nota < 3:
    print("Muy deficiente")
elif nota >= 3 and nota < 5:
    print("Insuficiente")
elif nota >= 5 and nota < 6:
    print("Suficiente")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota <= 10:
    print("Sobresaliente")
else:
    print("La nota ingresada no es válida.")
