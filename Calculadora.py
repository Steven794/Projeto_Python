import os
os.system('cls')

def soma(a, b):
    return a + b

def subtração(a, b):
    return a - b

def multiplicação(a, b):
    return a * b

def divisão(a, b):
    return a / b

continuar = 'S'

while continuar == 'S':
    numero1 = float(input("Digite o primeiro numero: "))
    numero2 = float(input("Digite o segundo numero: "))
    
    print("\n---Escolha a operação---\n1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão")
    opção = input("Digite qual operação você deseja realizar: ")
    
    if opção == '1':
        resultado = soma(numero1, numero2)
        print(f"Resultado: {resultado}")
        
    elif opção == '2':
        resultado = subtração(numero1, numero2)
        print(f"Resultado: {resultado}")
        
    elif opção == '3':
        resultado = multiplicação(numero1, numero2)
        print(f"Resultado: {resultado}")
        
    elif opção == '4':
        maior = max(numero1, numero2)
        menor = min(numero1, numero2)
        
        if menor == 0:
            print("Não é possível dividir por zero.")
        
        else:
            resultado = divisão(maior, menor)
            print(f"Resultado: {resultado}")
            
    else:
        print("Opção Inválida!")
        
    continuar = input("\nDeseja realizar outra operação (S/N)?").upper()
        
print("Encerrando Calculadora.")

#                                       .--.
#   ██╗     ██╗██████╗  ██████╗        |o_o |
#   ██║     ██║██╔══██╗██╔═████╗       |:_/ |
#   ██║     ██║██████╔╝██║██╔██║      //   \ \
#   ██║     ██║██╔══██╗████╔╝██║     (|     | )
#   ███████╗██║██║  ██║╚██████╔╝    /'\_   _/`\
#   ╚══════╝╚═╝╚═╝  ╚═╝ ╚══▀▀═╝     \___)=(___/