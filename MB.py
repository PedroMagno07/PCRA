# Lista de bebidas disponíveis
bebidas = [
    {"id": 1,"item": "Coca-Cola", "quantidade": 2, "preço": 3.75},
    {"id": 2,"item": "Pepsi", "quantidade": 5, "preço": 3.67},
    {"id": 3,"item": "Monster", "quantidade": 1, "preço": 9.96},
    {"id": 4,"item": "Café", "quantidade": 100, "preço": 1.25},
    {"id": 5,"item": "Redbull", "quantidade": 2, "preço": 13.99}
]

dinheiro = 0
loop = True

# exibe o estoque de bebidas
def mostrar_estoque():
    print("\nEstoque de Bebidas Atual:\n"
          "ID | BEBIDA | QTD |PREÇO")
    for produto in bebidas:
        print(f'{produto["id"]} | {produto["item"]} | {produto["quantidade"]} | R${produto["preço"]}')

# retorna bebida com base no ID
def buscar_bebida_por_id(id_bebida):
    for bebida in bebidas:
        if bebida["id"] == id_bebida:
            return bebida
    return None

# recebe o pagamento do usuário
def receber_pagamento(preco):
    pago = 0
    while pago < preco:  # até que o valor total seja suficiente
        valor_pago = float(input(f'Valor Pago: R$'))
        pago += valor_pago  # soma ao total pago

        if pago < preco:
            faltam = preco - pago
            print(f'Faltam R${faltam:.2f} para completar o pagamento.')
    return pago

# calcula e exibe o troco em notas e moedas
def calcular_e_exibir_troco(troco):
    notas = [200, 100, 50, 20, 10, 5, 2, 1]
    moedas = [0.50, 0.25, 0.10, 0.05, 0.01]

    print("\nSeu troco é de R${:.2f}, entregue da seguinte forma:".format(troco))

    troco_centavos = int(round(troco * 100))  # converte para centavos

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

# executa uma venda completa
def processar_venda():
    mostrar_estoque()
    try:
        id = int(input(f'\nSelecione uma das opções disponíveis: '))  # ID da bebida
    except ValueError:
        print("Entrada inválida. Use apenas números.")
        return

    preco = 0
    user_bebida = buscar_bebida_por_id(id)  # busca bebida pelo ID

    if user_bebida is None:
        print("\nID inválido.")
    elif user_bebida["quantidade"] <= 0:
        print(f'Item Esgotado.')
    else:
        preco = user_bebida["preço"]
        print(f'\nVocê Selecionou: {user_bebida["item"]} - R${preco:.2f}')
        pago = receber_pagamento(preco)  # recebe valor
        troco = pago - preco
        calcular_e_exibir_troco(troco)  # mostra troco

        print(f'\nPagamento aceito. Seu troco é R${troco:.2f}')
        user_bebida["quantidade"] -= 1  # atualiza estoque
        print(f'Bebida Retirada: {user_bebida["item"]}\n'
              f'Quantidade Restante: {user_bebida["quantidade"]}')

# loop principal da aplicação
while True:
    processar_venda()
