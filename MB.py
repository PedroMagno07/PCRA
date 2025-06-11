bebidas = [
    {"id": 1,"item": "Coca-Cola", "quantidade": 2, "preço": 3.75},
    {"id": 2,"item": "Pepsi", "quantidade": 5, "preço": 3.67},
    {"id": 3,"item": "Monster", "quantidade": 1, "preço": 9.96},
    {"id": 4,"item": "Café", "quantidade": 100, "preço": 1.25},
    {"id": 5,"item": "Redbull", "quantidade": 2, "preço": 13.99}
]

moedas = [
    {"valor": 5, "quantidade": 1},
    {"valor": 1, "quantidade": 1},
    {"valor": 0.20, "quantidade": 1},
    {"valor": 0.10, "quantidade": 1},
    {"valor": 0.01, "quantidade": 3}
]

dinheiro = 0

loop = True
def mostrar_estoque():
    print("\nEstoque de Bebidas Atual:\n"
          "ID | BEBIDA | QTD |PREÇO")
    for produto in bebidas:
        print(f'{produto['id']} | {produto['item'].capitalize()} | {produto['quantidade']} | R${produto['preço']}')


mostrar_estoque()

while True:

    id = int(input(f'\nSelecione uma das opções disponíveis: '))  # entrada da id do item selecionado pelo user
    preco = 0
    user_bebida = None
    pago = 0

    for item in bebidas:
        if item["id"] == id:  # se produto selecionado por id existe na matriz
            preco = item["preço"]  # definindo a variável preço
            user_bebida = item

    if user_bebida is None:
        print("\nID inválido.")

    elif user_bebida["quantidade"] <= 0:
        print(f'Item Esgotado.')

    else:

        print(f'\nVocê Selecionou: {user_bebida["item"]} - R${preco:.2f}')
        pago = float(input(f'R$: '))
        pago += dinheiro

while pago < preco:  # Loop infinito até o pagamento ser válido
        dinheiro = float(input(f'\n Faltam R${preco - pago:.2f}.\nInsira o valor faltante:\n'))
        faltam = preco - pago
        print(f'Valor: R${faltam:.2f}')

if pago > preco:

    troco = pago - preco
    print(f'\n'
            f'Seu troco é de: R${troco:.2f}')
    print('\nPagamento Válido')
    user_bebida["quantidade"] -= 1

else:
    print('\nPagamento Válido')
    user_bebida["quantidade"] -= 1

