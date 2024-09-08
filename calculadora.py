def somar(num1,num2):
    return num1 + num2
def subtrair(num1,num2):
    return num1 - num2
def multiplicar (num1,num2):
    return num1 * num2
def dividir (num1,num2):
        return num1 / num2
while True:
    print("escolha a operação:")
    print("1, somar")
    print("2, subtrair")
    print("3, multiplicar")
    print("4, dividir")
    print("5, sair")
   
    escolha = input("escolha:")
    if escolha == 5:
        break
    num1 = int(input("digite um numero:"))
    num2 = int(input("digite o segundo numero:"))
    if escolha == '1':
        print(f"resultado: {somar(num1, num2)}")
    elif escolha == '2':
        print(f"resultado: {subtrair(num1, num2)}")
    elif escolha == '3':
        print(f"resultado: {multiplicar(num1,num2)}")
    elif escolha == '4':
        print(f"resultado: {dividir(num1, num2)}")
    else:
        print("invalido")