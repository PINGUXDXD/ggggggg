print(
    ''''
    1.-pera 1200
    2.- manzana 1500
    3.- piña 2000

 ''')
select=int(print("seleccione una fruta: ")) 
if select==1:
      print("el total a pagar es de ", 1200*1.19)
else:
        if select==2:
          print("el total a pagar es de ", 1500*1.19)
        else: 
            if select==3:
               print("el total a pagar es de ", 2000*1.19)
            else 