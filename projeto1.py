menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=>  """

extrato = ""
saldo = 0
numero_saques = 0

while True:

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
