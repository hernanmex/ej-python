for i in range(1, 501):
    if i % 4 == 0:
        mensaje = str(i) + " (Múltiplo de 4)"
    elif i % 9 == 0:
        mensaje = str(i) + " (Múltiplo de 9)"
    else:
        mensaje = str(i)

    print(mensaje)

    if i % 5 == 0:
        print("------------------------------------------------------------")
