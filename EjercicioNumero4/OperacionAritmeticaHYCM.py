print("-----CALCULADORA H. CHOQUE M.-----")

#Datos de entrada
num1=int(input("Digite un numero:"))
num2=int(input("Digite el otro numero:"))
operacion=input("Digite la Operacion").upper()
#Proceso
if operacion=="+":
  suma=num1+num2
  print(f"\nLa suma es:{suma}")

elif operacion=="-":
  resta=num1-num2
  print(f"\nLa resta es:{resta}")

elif operacion=="/":
  div=num1/num2
  print(f"\nLa division es:{round(div,2)}")

elif operacion=="*":
  mult=num1*num2
  print(f"\nLa multiplicacion es:{mult}")

elif operacion=="^":
  potencia=num1**num2
  print(f"\nLa potencia es:{potencia}")

else:
  print("\nSe equivoco de operacion")
