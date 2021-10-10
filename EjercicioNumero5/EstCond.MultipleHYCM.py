print("-----Promedio Final-----")

#Datos de entrada
nota1=float(input("Ingrese nota 1:"))
nota2=float(input("Ingrese nota 2:"))
nota3=float(input("Ingrese nota 3:"))

#Proceso
if nota1<=20 and nota1>=0 and nota2<=20 and nota2>=0 and nota3<=20 and nota3>=0:

  promediofin=(nota1*0.25)+(nota2*0.25)+(nota3*0.50)
  print(f"Su promedio final es: {round(promediofin,2)}")

#AL EJERCICIO NUMERO 1 SE AGREGO CONDICIONES MULTIPLES:
#DONDE LAS NOTAS NO PUEDEN SER MAYOR A 20. 
#DONDE LAS NOTAS NO PUEDEN SER MENOS A 0.

elif nota1>20:
  print("La nota 1 no puede ser mayor a 20")
elif nota1<0:
  print("La nota 1 no puede ser menor a cero")
elif nota2>20:
  print("La nota 2 no puede ser mayor a 20")
elif nota2<0:
  print("La nota 2 no puede ser menor a cero")
elif nota3>20:
  print("La nota 3 no puede ser mayor a 20")
elif nota3<0:
  print("La nota 3 no puede ser menor a cero")
else:
  print("\ndatos incorrectos")
  
#SE COMPROBO  DICHAS  CONDICIONES.
#Hyerly Yhonson CHOQUE MAMANI
#COD : 202122854
