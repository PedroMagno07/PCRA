bebidas = [
    {"id": 1,"item": "Coca-Cola", "quantidade": 2, "preço": 3.75},
    {"id": 2,"item": "Pepsi", "quantidade": 5, "preço": 3.67},
    {"id": 3,"item": "Monster", "quantidade": 1, "preço": 9.96},
    {"id": 4,"item": "Café", "quantidade": 100, "preço": 1.25},
    {"id": 5,"item": "Redbull", "quantidade": 2, "preço": 13.99}
]

'''moedas = [
    {"valor": 200, "quantidade": 10},
    {"valor": 100, "quantidade": 1},
    {"valor": 50, "quantidade": 10},
    {"valor": 20, "quantidade": 10},
    {"valor": 10, "quantidade": 10},
    {"valor": 5, "quantidade": 10},
    {"valor": 2, "quantidade": 10},
    {"valor": 1, "quantidade": 10},
    {"valor": 0.20, "quantidade": 10},
    {"valor": 0.10, "quantidade": 10},
    {"valor": 0.05, "quantidade": 10},
    {"valor": 0.01, "quantidade": 10}
]'''

dinheiro = 0

loop = True
def mostrar_estoque():
    print("\nEstoque de Bebidas Atual:\n"
          "ID | BEBIDA | QTD |PREÇO")
    for produto in bebidas:
        print(f'{produto["id"]} | {produto["item"].capitalize()} | {produto["quantidade"]} | R${produto["preço"]}')



while True:

    mostrar_estoque()
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
        while pago < preco:  # Loop infinito até o pagamento ser válido
            valor_pago = float(input(f'Valor Pago: R$'))
            pago += valor_pago  # Atualiza o valor total pago

            if pago < preco:
                faltam = preco - pago
                print(f'Faltam R${faltam:.2f} para completar o pagamento.')

            elif pago >= preco:
                troco = pago - preco

                notas = [200, 100, 50, 20, 10, 5, 2, 1]
                moedas = [0.50, 0.25, 0.10, 0.05, 0.01]

                print("\nSeu troco é de R${:.2f}, entregue da seguinte forma:".format(troco))

                # Para evitar problemas com floats, trabalhar com centavos inteiros
                troco_centavos = int(round(troco * 100))

                for nota in notas:
                    nota_centavos = int(nota * 100)
                    qtd = troco_centavos // nota_centavos
                    if qtd > 0:
                        print(f'{qtd} nota(s) de R${nota}')
                        troco_centavos -= qtd * nota_centavos

                for moeda in moedas:
                    moeda_centavos = int(round(moeda * 100))
                    qtd = troco_centavos // moeda_centavos
                    if qtd > 0:
                        print(f'{qtd} moeda(s) de R${moeda:.2f}')
                        troco_centavos -= qtd * moeda_centavos

                print(f'\nPagamento aceito. Seu troco é R${troco:.2f}')
                user_bebida["quantidade"] -= 1
                print(f'Bebida Retirada: {user_bebida["item"]}\n'
                      f'Quantidade Restante: {user_bebida["quantidade"]}')



                break




