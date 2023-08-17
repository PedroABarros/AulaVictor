dicionario = {}
dicionario2 = {}

dicionario["nome"] = "Pedro"
dicionario["idade"] = "20"
dicionario["Telefone"] = "32 9087-6473"

dicionario2["nome"] = "Joao"
dicionario2["idade"] = "23"
dicionario2["Telefone"] = "32 3287-4373"

print(dicionario)
print(dicionario2)

print("-=" * 15)
for k, v in dicionario.items():
    print(k, v)

print("-=" * 15)
for k, v in dicionario2.items():
    print(k, v)