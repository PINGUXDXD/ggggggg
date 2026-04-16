# num=int(input("ingrese un numero: "))
# for i in range (num): 
#     print(i+1,"hola usuario ")
# num=int(input("ingrese un numero: "))
# for i in range(10):
#  print(num, "x", i+1 , "=", num*(i+1))

 
num=int(input("ingrese la cantidad de notas: "))
sum=0


for i in range(num):
  nota=float(input("ingresa la nota; "))
  sum=sum+nota
prom=sum/num
print("el promedio es", round(prom, 1))
if prom>=4.0:
  print("el alumno aprobo")
else:
  print("el alumno reprobo")
