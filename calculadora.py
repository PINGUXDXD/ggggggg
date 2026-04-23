def calculadora():
    print("--- Calculadora Pythonica ---")
    
    while True:
        print("\nOpciones:")
        print("1. Sumar (+)")
        print("2. Restar (-)")
        print("3. Multiplicar (*)")
        print("4. Dividir (/)")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == '5':
            print("¡Nos vemos! No rompas nada.")
            break

        
        try:
            num1 = float(input("Ingresa el primer número: "))
            num2 = float(input("Ingresa el segundo número: "))
        except ValueError:
            print("Error: Por favor, ingresa solo números válidos.")
            continue

        
        match opcion:
            case '1':
                resultado = num1 + num2
                print(f"Resultado: {num1} + {num2} = {resultado}")
            case '2':
                resultado = num1 - num2
                print(f"Resultado: {num1} - {num2} = {resultado}")
            case '3':
                resultado = num1 * num2
                print(f"Resultado: {num1} * {num2} = {resultado}")
            case '4':
                if num2 == 0:
                    print("Error: No puedes dividir por cero, el universo colapsaría.")
                else:
                    resultado = num1 / num2
                    print(f"Resultado: {num1} / {num2} = {resultado}")
            case _:
                print("Opción no válida. Intenta elegir algo del 1 al 5.")

if __name__ == "__main__":
    calculadora()