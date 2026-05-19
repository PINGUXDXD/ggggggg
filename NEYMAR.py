print("bienvenido a G2A")
tjuegos=0
indie=0
estudio=0
total=0
edad=0
while True:
    try:
        tjuegos=int(input("ingresa la cantidad de juegos que deseas comprar: "))
        if tjuegos<0:
            print("la cantidad de juegos debe ser un número positivo ")
        else:              
            break
    except ValueError:
        print("por favor ingresa un número válido")    
for i in range(tjuegos):
    while True:
        try:
            precio=float(input(f"ingresa el precio del juego {i+1}: "))
            if precio<0:
                print("el precio debe ser un número positivo ")
            else:
                break
        except ValueError:
            print("por favor ingresa un número válido")
    total+=precio
    tipo=input(f"ingresa el tipo del juego {i+1} (indie, estudio): ").lower()
    if tipo=="indie":
        indie+=1
    elif tipo=="estudio":
        estudio+=1

   