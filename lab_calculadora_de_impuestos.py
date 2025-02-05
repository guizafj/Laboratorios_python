#Calculadora de impuestos
income = float(input("Introduce el ingreso anual: "))

if income < 85528:
	tax = income * 0.18 - 556.02
# Calculo del impuesto cuando es superior a 85528
else:
    tax = (income - 85528) * 0.32 + 14839.02 # se aplica la regla de 14,839 pesos y 2 centavos, 
# más el 32% del excedente sobre 85,528 pesos.

if tax <= 0:
    tax = 0.0   

tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
