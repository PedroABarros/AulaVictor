from conta_corrente import ContaCorrente
from cliente import Cliente


conta1 = ContaCorrente(numero="12345", saldo_inicial=1000.0)
conta2 = ContaCorrente(numero="67890", saldo_inicial=500.0)


cliente1 = Cliente(nome=input("Digite o seu nome para o cadastro: "),
                   cpf="123.456.789-00")
cliente1.adicionar_conta(conta1)
cliente1.adicionar_conta(conta2)




print(conta1.depositar(int(input("Digite o valor que gostaria de depositar: "))))
print(conta2.sacar(int(input(f"Digite o valor que gostaria de sacar: "))))


for conta in cliente1.contas_correntes:
    print(f"Conta {conta.numero}: Saldo = R${conta.saldo:.2f}")