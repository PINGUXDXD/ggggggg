saldo = 100000
constante_monto = 5000

while True:
        print("\n--- CAJERO AUTOMÁTICO ---")
        print(f"1. Consultar saldo")
        print(f"2. Retirar dinero (Múltiplos de ${constante_monto})")
        print(f"3. Depositar dinero (Múltiplos de ${constante_monto})")
        print(f"4. Salir")
        
        try:
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                print(f"\nSu saldo actual es: ${saldo}")

            elif opcion == '2':
                monto = int(input(f"Monto a retirar (múltiplos de ${constante_monto}): "))
                
                if monto <= 0 or monto % constante_monto != 0:
                    raise ValueError(f"El monto debe ser positivo y múltiplo de ${constante_monto}.")
                if monto > saldo:
                    raise EOFError("Saldo insuficiente para realizar este retiro.")
                
                saldo -= monto
                print(f"Retiro exitoso. Su nuevo saldo es: ${saldo}")

            elif opcion == '3':
                monto = int(input(f"Monto a depositar (múltiplos de ${constante_monto}): "))
                
                if monto <= 0 or monto % constante_monto != 0:
                    raise ValueError(f"Solo se permiten depósitos en múltiplos de ${constante_monto}.")
                
                saldo += monto
                print(f"Depósito exitoso. Su nuevo saldo es: ${saldo}")

            elif opcion == '4':
                print("Gracias por usar el cajero. ¡Hasta pronto!")
                break

            else:
                raise IndexError("Opción no válida. Por favor, elija entre 1 y 4.")

        except ValueError as e:
            # Captura entradas no numéricas y montos que no cumplen la regla del múltiplo
            if "invalid literal for int()" in str(e):
                print("Error: Por favor, ingrese solo números enteros.")
            else:
                print(f"Error de monto: {e}")
        
        except EOFError as e:
            # Captura específicamente cuando el retiro excede el saldo
            print(f"Error de fondos: {e}")
            
        except IndexError as e:
            # Captura opciones fuera del menú
            print(f"Error de selección: {e}")
            
        except Exception as e:
            # Captura cualquier otro error inesperado
            print(f"Ocurrió un error inesperado: {e}")






