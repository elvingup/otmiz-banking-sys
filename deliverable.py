import textwrap

class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.limite_saque = 500
        self.numero_saques = 0
        self.limite_saques = 3

    def depositar(self, valor):
        """Deposita um valor na conta."""
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido. O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        """Saca um valor da conta."""
        if valor > self.saldo:
            print("Saldo insuficiente.")
        elif valor > self.limite_saque:
            print("Valor do saque excede o limite.")
        elif self.numero_saques >= self.limite_saques:
            print("Número máximo de saques excedido.")
        else:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            self.numero_saques += 1
            print("Saque realizado com sucesso!")

    def extrato(self):
        """Exibe o extrato da conta."""
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not self.extrato else self.extrato)
        print(f"Saldo: R$ {self.saldo:.2f}")
        print("==========================================")


def menu():
    """Apresenta o menu de opções para o usuário."""
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nu]\tNovo usuário
    [nc]\tNova conta
    [lc]\tListar contas
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))

def validar_cpf(cpf):
    """Valida um CPF utilizando o algoritmo de verificação."""
    cpf = str(cpf)

    # Elimina possíveis pontos e traços
    cpf = cpf.replace('.', '').replace('-', '')

    if len(cpf) != 11:
        return False

    # Primeira parte do cálculo do primeiro dígito verificador
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1

    # Segundo dígito verificador
    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito1 = 0
    else:
        digito1 = resto

    # Segunda parte do cálculo do segundo dígito verificador
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1

    resto = 11 - (soma % 11)
    if resto == 10 or resto == 11:
        digito2 = 0
    else:
        digito2 = resto

    # Verifica se os dígitos verificadores calculados batem com os dígitos informados
    digitos_verificadores = str(digito1) + str(digito2)
    return digitos_verificadores == cpf[-2:]

def criar_usuario(usuarios):
    """Cria um novo usuário e adiciona à lista de usuários."""
    cpf = input("Informe o CPF (somente números): ")
    while not validar_cpf(cpf):
        print("CPF inválido. Por favor, informe um CPF válido.")
        cpf = input("Informe o CPF (somente números): ")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço: ")
    novo_usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

contas = []
def criar_conta(agencia, numero_conta, usuarios):
    """Cria uma nova conta corrente e adiciona à lista de contas."""
    cpf = input("Informe o CPF do usuário: ")
    usuario = encontrar_usuario(cpf, usuarios)
    if usuario:
        nova_conta = ContaCorrente(agencia, numero_conta, usuario)
        contas.append(nova_conta)
        print("Conta criada com sucesso!")
    else:
        print("Usuário não encontrado.")

def encontrar_usuario(cpf, usuarios):
    """Encontra um usuário pela CPF."""
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None

def listar_contas(contas):
    """Lista todas as contas cadastradas."""
    if not contas:
        print("Não há contas cadastradas.")
        return
    for conta in contas:
        print(f"Agência: {conta.agencia}")
        print(f"Número da conta: {conta.numero_conta}")
        print(f"Titular: {conta.usuario.nome}")
        print("-" * 30)

def main():
    """Função principal do programa."""
    agencia = "0001"
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == 'd':
            valor = float(input("Informe o valor do depósito: "))
            ContaCorrente.depositar(valor)  # Chamada à função de depósito

        elif opcao == 's':
            valor = float(input("Informe o valor do saque: "))
            ContaCorrente.sacar(valor)  # Chamada à função de saque

        elif opcao == 'e':
            ContaCorrente.extrato()
        elif opcao == 'nu':
            criar_usuario(usuarios)
        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            criar_conta(agencia, numero_conta, usuarios)
        elif opcao == 'lc':
            listar_contas(contas)
        elif opcao == 'q':
            break
        else:
            print("Opção inválida.")

'''
__name__ representa o nome do módulo atual. Se o módulo está sendo executado diretamente (não importado), __name__ é definido como "__main__".
if __name__ == "__main__" verifica se o módulo está sendo executado diretamente. Se for verdade, o bloco de código dentro da condição será executado.
Se o módulo for importado, o bloco de código dentro da condição não será executado.
'''
if __name__ == "__main__":
    main()