print("Calcular potencia")
base = int(input("Ingresa la base: "))
exponente = int(input("Ingresa el exponente: "))
resultado = 1 
for i in range(exponente):
    resultado = resultado * base
print("Resultado:", resultado)