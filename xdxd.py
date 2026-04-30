total=0
op=0
cantper=0
while op!=4:
  print("""
    1.- niño (1-17) $1000
    2.- adultos (18-64) $3000
    3.- adultos mayaores (64+) $1500
    4.- salir """)
  op=int(input("ingrese opcion "))
  
  match op:

    case 1:
      print("pagando el precio del niño ")
      c=int(input("cuantos son?: "))
      total=1000*c
      while c<1 or c>10:
        print ()
        