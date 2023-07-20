import time
menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
print(f"{' Seja bem vindo ao sistema! '.center(45,'=')}")
# Variáveis
saldo = 0
deposito = 0
extrato = ""
LIMITE_SAQUES = 2
num_saques = 0
limite = 500
valor = 0

while True:
    time.sleep(0.5)
    escolha = input(f"{menu}Qual será sua escolha?: => ")
    escolha = escolha.lower().strip() # deixa minúsculo e tira os parênteses caso tenha.
    # DEPOSITO
    if escolha == 'd':
        valor = float(input("Digite o valor do depósito => "))

        if valor > 0:
            saldo += valor
            extrato = extrato+(f'Depósito: R$ {valor:.2f}\n')
            print(f'Depósito de R$ {valor:.2f} realizado.')
            time.sleep(1)
        else:
            print("Valor inválido! Tente novamente.")
            time.sleep(1)
    # SAQUE
    elif escolha == 's':
        if num_saques > LIMITE_SAQUES: # Verifica se não passou do limite de saques.
            print("Você excedeu o limite de saques.")
            time.sleep(1)
            continue
        valor = float(input("Digite o valor do saque => "))
        if valor > limite:
            print("Você só pode realizar um saque único de até $500.00! ")
            time.sleep(1)
            continue
        if valor > saldo:
            print("Você não tem saldo suficiente.")
            time.sleep(1)
            continue
        if valor > 0:
            saldo -= valor
            extrato = extrato+(f'Saque: R$ {valor:.2f}\n')
            print(f'Saque de R$ {valor:.2f} realizado.')
            time.sleep(1)
            num_saques += 1
        else:
            print("Valor inválido, tente novamente.")
            time.sleep(1)
            continue

    # EXTRATO    
    elif escolha == 'e':
        time.sleep(1)
        print(f"{' EXTRATO '.center(30,'=')}")
        print(f' SALDO: R$ {saldo:.2f} '.center(30,'='))
        print("Não foram realizadas movimentações." if not extrato else extrato) # Se extrato estiver vazio, se não - print (extrato)
        print(f"{' FIM '.center(30,'=')}")
    # SAIDA
    elif escolha == 'q':
        print(" PROGRAMA FINALIZADO. ".center(30,'=')) 
        break
    else:
        print("Escolha inválida, tente novamente.")
print(f' OBRIGADO POR UTILIZAR! :)'.center(30,'='))  
print(extrato)  