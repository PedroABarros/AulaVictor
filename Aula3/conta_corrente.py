# Criar contas correntes
# Criar cliente e adicionar contas
# Realizar operações nas contas do cliente
# Consultar contas do cliente
        

class ContaCorrente:
    def __init__(self):
        self.numero = ""
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            return f"Depósito de R${valor:.2f} da conta {ContaCorrente(self.numero)} realizado. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Valor inválido para depósito."

    def sacar(self, valor):
        if valor < self.saldo:
            self.saldo -= valor
            return f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}"
        else:
            return "Saldo insuficiente ou valor inválido para saque."

    def consultar_saldo(self):
        return f"Saldo atual: R${self.saldo:.2f}"
