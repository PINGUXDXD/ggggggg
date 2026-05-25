saldo=100000
constante=5000
while True:
    print("bienvenido al cajero automatico ")
    print(f"1.- consultar saldo ")
    print(f"2.- retirar dinero: ${constante}")
    print(f"3.- depositar dinero: ${constante}")
    print(f"4.- salir ")

    try:
        op = input("elija una opcion ")  
        if op == '1':
            print(f"su saldo actual es: ${saldo}")
        elif op == '2':
            monto = int(input(f"monto a retirar (multiplo de ${constante}): "))
            if monto <= 0 or monto % constante != 0:
                raise ValueError(f"el monto debe ser positivo y multiplo de ${constante}")
            if monto > saldo:
                raise EOFError("saldo insuficiente para realizar este retiro")
            saldo -= monto
            print(f"retiro exitoso. su nuevo saldo es: ${saldo}")
        elif op == '3':
            monto = int(input(f"monto a depositar (multiplo de ${constante}): "))
            if monto <= 0 or monto % constante != 0:
                raise ValueError(f"solo se permiten depositos en multiplos de ${constante}")
            saldo += monto
            print(f"deposito exitoso. su nuevo saldo es: ${saldo}")
        elif op == '4':
            print("gracias por usar el cajero, hasta pronto")
            break
        else:
            raise IndexError("opcion no valida, por favor elija entre 1 y 4")

    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("error: por favor ingrese solo numeros enteros")
        else:
            print(f"error de monto: {e}")    
    except EOFError as e:
        print(f"error de fondos: {e}")
    except IndexError as e:
        print(f"error de seleccion: {e}")   
    except Exception as e:
        print(f"error inesperado: {e}")

        
