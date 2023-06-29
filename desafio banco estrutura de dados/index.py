def main():
  print("Seja bem-vindo ao Banco do Note!!\nEscolha uma das opções abaixo..")
  num_conta = 0
  num = 1
  contas = {}
  usuarios = {}
  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  LIMITE_SAQUES = 3

  while True:
    opcao = menu()
    if opcao == "s":
      valor = float(input("Informe o valor do saque: "))
      saldo, extrato = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, LIMITE_SAQUES=LIMITE_SAQUES)
    elif opcao == "d":
      valor = float(input("Informe o valor do depósito: "))
      saldo, extrato = depositar(saldo, valor, extrato)
    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)
    elif opcao == "nc":
      
      print("Antes da criação da conta, é necessário algumas informações: ")
      cliente = input("Por favor, informe o seu nome: ")
      ja_tem_conta = input("Digite 1 se o senhor não tem uma conta nesse banco e 2 se já tiver: ")
      if ja_tem_conta == "2":
        confirmacao_numero_conta = int(input("Qual o número da conta? "))
        if confirmacao_numero_conta == contas[cliente]["Contas"]["Número da conta"]:
          confirmacao = input("O senhor tem certeza que deseja criar outra conta relacionada a esse usuario? Digite 1 para sim e 2 para não.. ")
          if confirmacao == "1":
            pessoa = input("Qual nome de usuario está cadastrado no sistema? Digite 2 se não ter cadastro. ")
            if pessoa == "2":
              desejo = input("Para criar uma conta o Sr. precisa ter um usuario cadastrado, deseja cadastrar agr? Digite 1 para SIM e 2 para NÃO. ")
              if desejo == "1":
                print("Certo, o Sr. será redirecionado para a aba de cadastro de usúarios.")
                cliente = input("Qual o nome do Sr.? ")
                criar_usuario(cliente, usuarios)
              elif desejo == "2":
                print("Certo, o Sr. será redirecionado para o inicio então.")

            else:
              chaves = [usuarios.keys()]
              for item in chaves:
                if pessoa == item:
                  confirmacao_cpf = input("Qual o cpf da sua conta? ")
                  if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                    num_conta, num = criar_conta(num_conta, num)
                    contas[cliente]["Contas"][f"Conta{num}"] = {f"Usuario{num}": pessoa, f"Agência{num}": "0001",   
                    f"Número da conta{num}": num_conta}
                    print("=== A conta do senhor foi criada com sucesso!! ===")
                    print(contas[cliente])
                  elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                    print("CPF não encontrado/n O Sr. tem mais uma tentativa.")
                    confirmacao_cpf = input("CPF: ")
                    if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                      num_conta, num = criar_conta(num_conta, num)
                      contas[cliente]["Contas"][f"Conta{num}"] = {f"Usuario{num}": pessoa, f"Agência{num}": "0001",   
                      f"Número da conta{num}": num_conta}
                      print("=== A conta do senhor foi criada com sucesso!! ===")
                      print(contas[cliente])
                    elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                      print("CPF não encontrado. BLOQUEADO!!")
                      break
                elif pessoa != item:
                  print("Usuario não encontrado..")
          
          elif confirmacao == "2":
            print("Certo, muito obrigado por todo suporte!!")
        elif confirmacao_numero_conta != contas[cliente]["Contas"]["Número da conta"]:
          confirmacao_numero_conta = int(input("Número nao registrado, o senhor só tem mais uma tentativa: "))
          if confirmacao_numero_conta == contas[cliente]["Contas"]["Número da conta"]:
            confirmacao = input("O senhor tem certeza que deseja criar outra conta relacionada a esse usuario? Digite 1 para sim e 2 para não.. ")
            if confirmacao == "1":
              pessoa = input("Qual nome de usuario está cadastrado no sistema? Digite 2 se não ter cadastro. ")
              if pessoa == "2":
                desejo = input("Para criar uma conta o Sr. precisa ter um usuario cadastrado, deseja cadastrar agr? Digite 1 para SIM e 2 para NÃO. ")
                if desejo == "1":
                  print("Certo, o Sr. será redirecionado para a aba de cadastro de usúarios.")
                  cliente = input("Qual o nome do Sr.? ")
                  criar_usuario(cliente, usuarios)
                elif desejo == "2":
                  print("Certo, o Sr. será redirecionado para o inicio então.")
                  return
              else:
                chaves = usuarios.keys()
                for item in chaves:
                  if pessoa == item:
                    confirmacao_cpf = input("Qual o cpf da sua conta? ")
                    if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                      num_conta, num = criar_conta(num_conta, num)
                      contas[cliente]["Contas"][f"Conta{num}"] = {f"Usuario{num}": item, f"Agência{num}": "0001",   
                      f"Número da conta{num}": num_conta}
                      print("=== A conta do senhor foi criada com sucesso!! ===")
                      print(contas[cliente])
                    elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                      print("CPF não encontrado/n O Sr. tem mais uma tentativa.")
                      confirmacao_cpf = input("CPF: ")
                      if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                        num_conta, num = criar_conta(num_conta, num)
                        contas[cliente]["Contas"][f"Conta{num}"] = {f"Usuario{num}": pessoa, f"Agência{num}": "0001",   
                        f"Número da conta{num}": num_conta}
                        print("=== A conta do senhor foi criada com sucesso!! ===")
                        print(contas[cliente])
                      elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                        print("CPF não encontrado. BLOQUEADO!!")
                        break
                  elif pessoa != item:
                    print("Usuario não encontrado..")
                      
                  

                
            elif confirmacao == "2":
              print("Certo, muito obrigado por todo suporte!!")
          elif confirmacao_numero_conta != contas[cliente]["Contas"]["Número da conta"]:
            print("Número não encontrado, BLOQUEADO!!")
            break
            
      elif ja_tem_conta == "1":
        pessoa = input("Qual nome de usuario está cadastrado no sistema? Digite 2 se não ter cadastro. ")
        if pessoa == "2":
          desejo = input("Para criar uma conta o Sr. precisa ter um usuario cadastrado, deseja cadastrar agr? Digite 1 para SIM e 2 para NÃO. ")
          if desejo == "1":
            print("Certo, o Sr. será redirecionado para a aba de cadastro de usúarios.")
            cliente = input("Qual o nome do Sr.? ")
            criar_usuario(cliente, usuarios)
          elif desejo == "2":
            print("Certo, o Sr. será redirecionado para o inicio então.")
                
        else:
          chaves = usuarios.keys()
          for item in chaves:
            if pessoa == item:
              confirmacao_cpf = input("Qual o cpf da sua conta? ")
              if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                num_conta, num = criar_conta(num_conta, num)
                main_user = input("Qual será o main_user do senhor? ")
                contas[cliente] = {"Main_User": main_user, "Contas": {"Usuario": item, "Agência": "0001", "Número da conta": num_conta}}
                print("=== A conta do senhor foi criada com sucesso!! ===")
                print(contas[cliente])
              elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                print("CPF não encontrado/n O Sr. tem mais uma tentativa.")
                confirmacao_cpf = input("CPF: ")
                if usuarios[pessoa]["CPF"] == confirmacao_cpf:
                  num_conta, descartavel = criar_conta(num_conta, num)
                  main_user = input("Qual será o main_user do senhor? ")
                  contas[cliente] = {"Main_User": main_user, "Contas": {"Usuario": item, "Agência": "0001", "Número da conta": num_conta}}
                  print("=== A conta do senhor foi criada com sucesso!! ===")
                  print(contas[cliente])
                elif usuarios[pessoa]["CPF"] != confirmacao_cpf:
                  print("CPF não encontrado. BLOQUEADO!!")
                  break
            elif pessoa != item:
              print("Usuario não encontrado..")
  
    elif opcao == "lc":
      pass
    elif opcao == "nu":
      print("É necessário algumas informações para a conta do Sr. ser criada..\nPreencha os campos abaixo por favor.")
      cliente = input("Qual nome o Sr. deseja ser endereçado? ")
      nome, data_de_nascimento, cpf, endereco = criar_usuario(cliente, usuarios)
      usuarios[nome] = {"Identificação": nome, "Data de nascimento": data_de_nascimento, "CPF": cpf, "Endereço": endereco}
        
      print("=== O usuário foi criado com sucesso!! ===")
      print(usuarios)
    elif opcao == "q":
      print("=== Muito obrigado pela preferência, volte sempre!! ===")
      break
    else:
      print("@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")

def menu():
  menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[Lc] Listar conta
[nu] Novo Usuario
[q] Sair
=> """
  opcao = input(menu)
  return opcao

def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

  excedeu_saldo = valor > saldo

  excedeu_limite = valor > limite

  excedeu_saques = numero_saques >= LIMITE_SAQUES

  if excedeu_saldo:
    print("@@@ Operação falhou! Você não tem saldo suficiente. @@@")

  elif excedeu_limite:
    print("@@@ Operação falhou! O valor do saque excede o limite. @@@")

  elif excedeu_saques:
    print("@@@ Operação falhou! Número máximo de saques excedido. @@@")

  elif valor > 0:
    saldo -= valor
    extrato += f"Saque:\t\t\tR$ {valor:.2f}\n"
    numero_saques += 1
    print("=== Saque realizado com sucesso!! ===")

  else:
    print("@@@ Operação falhou! O valor informado é inválido. @@@")

  return saldo, extrato

def depositar(saldo, valor, extrato, /):

  if valor > 0:
    saldo += valor
    extrato += f"Depósito:\t\tR$ {valor:.2f}\n"
    print("=== Depósito realizado com sucesso!! ===")
    
  else:
      print("@@@ Operação falhou! O valor informado é inválido. @@@")

  return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
  print("\n================ EXTRATO ================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
  print("==========================================")

def criar_usuario(cliente, usuarios):
  data_de_nascimento = input("Data de nascimento: ")
  cpf = input("Por favor, informe o seu CPF: ")
  for valor in usuarios.values():
    if "CPF" in valor:
      if cpf != valor["CPF"]:
        pass
      else:
        print("@@@ CPF já registrado, por favor realize o processo novamente e informe um CPF q nao esta registrado em nosso sistema. @@@")
        criar_usuario(cliente, usuarios)
  logradouro = input("logradouro: ")
  nro = input("Número da residência: ")
  bairro = input("Bairro:")
  cidade = input("Cidade: ")
  estado = input("Estado(Sigla, ex:GO, BH...): ")
  endereco = logradouro + ", " + nro + " - " + bairro + " - " + cidade + "/" + estado
  print("=== Usuário criado com sucesso!! ===")
  return cliente, data_de_nascimento, cpf, endereco

def criar_conta(num_conta, num):
  print("A conta do Sr. está sendo criada, aguarde um momento..")
  num_conta += 1
  num += 1
  return num_conta, num
