while True:
    operacija = input("Izberite operacijo: sestevanje(1), odstevanje(2), mnozenje(3), prekinitev(0): ")
    if operacija == 0:
        break
    a = input("prva stevilka: ")
    b = input("druga stevilka ")
    if operacija == 1:
        print("Rezultat je: " + str(a+b))
    elif operacija == 2:
        print("Rezultat je: ") + str(a-b)
    elif operacija == 3:
        print("Rezultat je: " + str(a*b))
    else:
        print("Operacija ni definirana!")
    print("Novi vnos")    