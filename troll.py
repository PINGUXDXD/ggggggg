print("1.- pc $500.000")
print("2.- LGTV de 55 pulgadas $450.000")
print("3.- Microondas mademsa $100.000")
print("4.- salir")
print("seleccione una opcion ")
op=int(input())
match op:
    case 1:
        print("el total a pagar es ", 500000*1.19)
    case 2:
        print("el total a pagar es ", 450000*1.19)
    case 3:
        print("el total a pagar es ", 100000*1.19)
    case 4:
        print("saliendo") 