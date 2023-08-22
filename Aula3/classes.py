# Criar contas correntes
# Criar cliente e adicionar contas
# Realizar operações nas contas do cliente
# Consultar contas do cliente
        

class ContaCorrente:
    def __init__(self, numero, saldo_inicial=0.0):
        self.numero = numero
        self.saldo = saldo_inicial

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Valor inválido para depósito."

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Saldo insuficiente ou valor inválido para saque."

    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"


class Cliente:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf
        self.contas_correntes = []

    def adicionar_conta(self, conta):
        self.contas_correntes.append(conta)
        return f"Conta {conta.numero} adicionada para o cliente {self.nome}"
    


conta1 = ContaCorrente(numero="12345", saldo_inicial=1000.0)
conta2 = ContaCorrente(numero="67890", saldo_inicial=500.0)


cliente1 = Cliente(nome=input("Digite o seu nome para o cadastro: "),
                   cpf=input("Digite o seu cpf para cadastro: "))
cliente1.adicionar_conta(conta1)
cliente1.adicionar_conta(conta2)


print(conta1.depositar(int(input("Digite o valor que gostaria de depositar: "))))
print(conta2.sacar(int(input(f"Digite o valor que gostaria de sacar: "))))


for conta in cliente1.contas_correntes:
    print(f"Conta {conta.numero}: Saldo = R${conta.saldo:.2f}")
 






