# Jeito 1
jeito1 = False

menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=>  """

extrato = ""
saldo = 0
numero_saques = 0

while jeito1:

    opcao = input(menu)

    if opcao == "0":
        deposito = float(input("Qual valor deseja depositar? "))
        if deposito < 0.25:
            print("Por favor, deposito permitido apenas de 25 centavos para cima..")
        elif deposito >= 0.25:
            print("Deposito realizado com sucesso!!")
            saldo += deposito
            extrato += f"Depósito: R$ {deposito:.2f}\n"
        
        

    elif opcao == "1":
        if numero_saques < 3:
            saque = float(input("Qual a quantia que deseja sacar? "))
            if saque > saldo:
                print("Sem saldo o suficiente..")
            elif saque > 500:
                print("limite maximo de saque é R$500,00")
            else:
                print("Saque realizado com sucesso!")
                extrato += f"Saque: R$ {saque:.2f}\n"
        else:
            print("Número maximo de saques diario atingido!!")
                
            

    elif opcao == "2":
        print("\n=============== Extrato ==================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("============================================")

    elif opcao == "3":
        print("Muito obrigado por usar nosso banco!! Volte sempre!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")

# Jeito 2

jeito2 = False

menu2 = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=>  """

saldo2 = 0
limite2 = 500
extrato2 = ""
numero_saques2 = 0
LIMETE_SAQUES = 3

while jeito2:

    opcao2 = input(menu2)

    if opcao2 == "0":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo2 += valor
            extrato2 += f"Depósito: R$ {valor:.2f}\n"
            print("Depósito realizado com sucesso!!")

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao2 == "1":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo2

        excedeu_limite = valor > limite2

        excedeu_saque = numero_saques2 >= LIMETE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saque:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo2 -= valor
            extrato2 += f"Saque: R$ {valor:.2f}\n"
            numero_saques2 += 1
            print("Saque realizado com sucesso!!")

        else:
            print("Operação falhou! O valor informado é inválido.")
    
    elif opcao2 == "2":
        print("\n=============== Extrato ==================")
        print("Não foram realizadas movimentações." if not extrato2 else extrato2)
        print(f"\nSaldo: R$ {saldo2:.2f}")
        print("============================================")

    elif opcao2 == "3":
        print("Muito obrigado pela preferência, volte sempre!!")
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")