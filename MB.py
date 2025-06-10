bebidas = [
    {"id": 1,"item": "Coca-Cola", "quantidade": 2, "preço": 3.75},
    {"id": 2,"item": "Pepsi", "quantidade": 5, "preço": 3.67},
    {"id": 3,"item": "Monster", "quantidade": 1, "preço": 9.96},
    {"id": 4,"item": "Café", "quantidade": 100, "preço": 1.25},
    {"id": 5,"item": "Redbull", "quantidade": 2, "preço": 13.99}
]

dinheiro = 0

loop = True
def mostrar_estoque():
    print("\nEstoque de Bebidas Atual:\n"
          "ID | BEBIDA | QTD |PREÇO")
    for produto in bebidas:
        print(f'{produto['id']} | {produto['item'].capitalize()} | {produto['quantidade']} | R${produto['preço']}')


print(mostrar_estoque())

id = int(input(f'\nSelecione uma das opções disponíveis: ')) #entrada da id do item selecionado pelo user
preco = 0
user_bebida = None


for item in bebidas:
    if item["id"] == id: #se produto selecionado por id existe na matriz
        preco = item["preço"] #definindo a variável preço
        user_bebida = item["item"]


    #PAGAMENTO



if preco is None:
        print("ID inválido. Produto não encontrado.")
else:
        dinheiro = float(input(f'\n'
                               f'Pague o produto selecionado:\n'
                               f'{user_bebida} R${preco:.2f}: '))  # Mostra o preço correto
while True:  # Loop infinito até o pagamento ser válido

            #NÃO ESTÁ ACUMULANDO O VALOR PAGOOOOOOOOOOOOOOOOOOOOOOOOOO
        if dinheiro < preco:
                faltam = preco - dinheiro
                print(f'\n'
                      f'Faltam: R${faltam}')

        if dinheiro > preco:

                troco = dinheiro - preco
                print(f'\n'
                      f'Seu troco é de: R${troco:.2f}')
                print('Pagamento Válido')

        else:

                print('Pagamento Válido')
        break