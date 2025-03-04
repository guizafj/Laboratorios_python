#Calculadora de impuestos
ng_income = float(input("Introduce el ingreso anual: "))

if ng_income < 85528:
	ng_tax = ng_income * 0.18 - 556.02
# Calculo del impuesto cuando es superior a 85528
else:
    ng_tax = (ng_income - 85528) * 0.32 + 14839.02 # se aplica la regla de 14,839 pesos y 2 centavos, 
# más el 32% del excedente sobre 85,528 pesos.

if ng_tax <= 0:
    ng_tax = 0.0   

ng_tax = round(ng_tax, 0)
print("El impuesto es:", ng_tax, "pesos")
