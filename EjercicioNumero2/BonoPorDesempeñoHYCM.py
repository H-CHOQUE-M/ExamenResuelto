print("-----Bono Por Desenpeño-----")
#Datos de entrada
bono=int(input("Ingrese puntos:"))


#Proceso
if bono >= 100 and bono<=200:
  bonofin=(bono*0.10)
  print(f"Su bono final es: {round(bonofin,2)}")

elif bono >= 201 and bono<=300:
  bonofin=(bono*0.40)
  print(f"Su bono final es: {round(bonofin,2)}")

elif bono >=301 and bono<=400:
  bonofin=(bono*0.70)
  print(f"Su bono final es: {round(bonofin,2)}")

elif bono >=401:
  bonofin=(bono*0.80)
  print(f"Su bono final es: {round(bonofin,2)}")

else:
  print("\nNo le corresponde ningun bono")
