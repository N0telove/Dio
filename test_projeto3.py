from abc import ABC, abstractmethod, abstractproperty
from datetime import datetime
import textwrap

class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    def saldo(self):
        return self._saldo

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
        

    def sacar(self, valor):
        excedeu_saldo = valor > self._saldo

        if excedeu_saldo:
           print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

        elif valor > 0:
            self._saldo -= valor
            print("\n=== Saque realizado com sucesso! ===")
            return True

        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

        return False


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("\n=== Depósito realizado com sucesso! ===")
        else:
            print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
            return False

        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self._limite = float(input("Informe o limite desejado da sua conta: "))
        self._limite_saques = int(input("Informe o limite de saques desejado da sua conta: "))


    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        excedeu_limite = valor > self._limite
        excedeu_saques = numero_saques >= self._limite_saques

        if excedeu_limite:
            print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

        elif excedeu_saques:
            print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

        else:
            return super().sacar(valor)

        return False
        
    def __str__(self):
        return f"""\
            Agência:\t{self._agencia}
            C/C:\t\t{self._numero}
            Titular:\t{self.cliente._nome}"""

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )




class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

    @abstractmethod
    def valor(self):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = float(valor)

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        self._cpf = cpf
        self._nome = nome
        self._data_nascimento = data_nascimento
        super().__init__(endereco)


def menu():
    menu = """\n
    ================ MENU ===============
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo usúario
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def filtrar_clientes(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente._cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("\n@@@ Cliente não possui conta! @@@")
        return 

    # FIXME: não permite cliente escolher a conta
    numero_conta = int(input("Informe o numero da conta do Sr. "))
    # conta = [conta for conta in cliente.contas if conta._numero == numero_conta]
    # for conta in cliente.contas:
    #     if conta._numero != numero_conta:
    #         conta = cliente.contas

    print(cliente.contas[numero_conta - 1])
    return cliente.contas[numero_conta - 1]

def validacao(clientes, retorna=0):
    cpf = input("Informe o CPF do cliente: ")
    cliente = filtrar_clientes(cpf, clientes)


    if retorna == 0:
        if not cliente:
            print("\n@@@ Cliente não encontrado! @@@")
            return 0
    
    elif retorna == 1:
 
        if cliente:
            print("\n@@@ Já existe cliente com esse CPF! @@@")
            return 1, None
        
        return cliente, cpf

    elif retorna == 2:

        if not cliente:
            print("\n@@@ Cliente não encontrado, fluxo de criação de conta encerrado! @@@")
            return 2

    return cliente


def recuperacao(cliente, transacao):
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def depositar(clientes):
    cliente = validacao(clientes)
    if cliente == 0:
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = Deposito(valor)

    recuperacao(cliente, transacao)


def sacar(clientes):
    cliente = validacao(clientes)
    if cliente == 0:
        return


    try:  
        valor = float(input("Informe o valor do saque: "))
    except:
        print("O Sr. será redirecionado, na proxima insira um valor adequado.. ")
        return
    transacao = Saque(valor)

    recuperacao(cliente, transacao)


def exibir_extrato(clientes):
    cliente = validacao(clientes)
    if cliente == 0:
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("\n=============== Extrato ==================")
    Transacoes = conta.historico.transacoes

    extrato = ""
    if not Transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in Transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")
    print("============================================")

def criar_cliente(clientes):
    cliente, cpf = validacao(clientes, 1)
    if cliente == 1:
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    logradouro = input("logradouro: ")
    nro = input("Número da residência: ")
    bairro = input("Bairro:")
    cidade = input("Cidade: ")
    estado = input("Estado(Sigla, ex:GO, BH...): ")
    endereco = logradouro + ", " + nro + " - " + bairro + " - " + cidade + "/" + estado

    cliente = PessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)

    clientes.append(cliente)

    print("\n=== Cliente criado com sucesso! ===")

def criar_conta(numero_conta, clientes, contas):
    cliente = validacao(clientes, 2)
    if cliente == 2:
        return


    numero = len(cliente.contas[0:]) + 1
    conta = ContaCorrente.nova_conta(cliente=cliente, numero=numero)
    contas.append(conta)
    cliente.contas.append(conta)

    print("\n=== Conta criada com sucesso! ===")


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            depositar(clientes)

        elif opcao == "s":
            sacar(clientes)

        elif opcao == "e":
            exibir_extrato(clientes)

        elif opcao == "nu":
            criar_cliente(clientes)
        
        elif opcao == "nc":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("=== Muito obrigado pela preferência, volte sempre!! ===")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação deseajada. @@@")

main()