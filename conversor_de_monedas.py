#!/usr/bin/python

def convertir_monedas(moneda , valorusd):
    cantidad = float(input(f"¿Cuantos {moneda} tienes?: "))
    dolares= round(valorusd*cantidad,5)
    print(f"tienes {dolares} dolares")

menu = """ 
Bienvenido al conversor de monedas

1-Euros a Dolares
2-Rublos Rusos a Dolares
3-Pesos Mexicanos a Dolares
4-Pesos Colombianos a Dolares
Selecciona una opción: """

opción = input(menu)

if opción == "1":
    convertir_monedas("euros", 1.16)

elif opción =="2":
    convertir_monedas("Rublos rusos",0.014)
elif opción == "3":
    convertir_monedas("Pesos mexicanos",0.048)
elif opción == "4":
    convertir_monedas("Pesos colombianos",0.00027)
else:
    print("elige una opción valida")
