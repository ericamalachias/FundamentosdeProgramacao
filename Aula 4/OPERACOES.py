#Programa Calculadora com IF-ELIF-ELSE
#10/03/26

fv = input("Digite 1-SOMA, 2-SUBTRAÇÃO, 3-DIVISÃO, 4-MULTIPLICAÇÃO, 5-POTENCIAÇÃO, 6-RADICIAÇÃO")
fv = int(fv)

a = input("Entre com o 1° número")
a = int(a)

b = input("Entre com o 2°  número")
b = int(b)

if (fv == 1):
    print(a + b)
    
elif(fv == 2):
    print(a - b)
    
elif(fv == 3):
    print(a / b)
    
elif(fv == 4):
    print(a * b)
    
elif(fv == 5):
    print(a ** b)
    
elif(fv == 6):
    print(a ** (1/2))

else:
    print("Digite uma opção válida")



input()