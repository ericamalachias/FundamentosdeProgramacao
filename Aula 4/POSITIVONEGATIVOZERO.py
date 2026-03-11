#Número negativo, positivo ou zero.
#10/03/26

a = input("Informe um número")
a = int(a)

if(a > 0):
    print("Positivo")
elif(a < 0):
    print("Negativo")
elif(a == 0):
    print("Zero")
    
else:
    print("Digite um número válido")

input()