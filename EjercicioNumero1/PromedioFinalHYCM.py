print("-----Promedio Final-----")

#Datos de entrada
nota1=float(input("Ingrese nota 1:"))
nota2=float(input("Ingrese nota 2:"))
nota3=float(input("Ingrese nota 3:"))

#Proceso
promediofin=(nota1*0.25)+(nota2*0.25)+(nota3*0.50)
#Datos de salida
print(f"Su promedio final es: {round(promediofin,2)}")