estoque_produtos = [
    {
        "nome": "Teclado",
        "quantidade": 10,
        "preco": 150.00
    },
    {
        "nome": "Mouse",
        "quantidade": 20,
        "preco": 80.50
    },
    {
        "nome": "Monitor",
        "quantidade": 5,
        "preco": 700.00
    }
]

# Loop principal do sistema de estoque
while True:

    # Exibe o menu de opções ao usuário
    print("\n===== SISTEMA DE CONTROLE DE ESTOQUE =====")
    print("1 - Estoque atual")
    print("2 - Entrada de produtos")
    print("3 - Saída de produtos")
    print("4 - Sair")

    # Coleta a opção digitada pelo usuário
    opcao_usuario = input("Digite a opção desejada: ")

    # Opção 1 - Visualizar estoque atual
    if opcao_usuario == "1":

        print("\n===== ESTOQUE ATUAL =====")

        # Percorre todos os itens da lista
        for produto in estoque_produtos:

            print(f"Produto: {produto['nome']}")
            print(f"Quantidade: {produto['quantidade']}")
            print(f"Preço: R$ {produto['preco']:.2f}")
            print("----------------------")

    # Opção 2 - Registrar entrada de produtos
    elif opcao_usuario == "2":

        nome_produto = input("Digite o nome do produto: ")

        # Converte o valor digitado de string para inteiro
        quantidade_entrada = int(input("Digite a quantidade de entrada: "))

        produto_encontrado = False

        # Percorre a lista procurando o produto informado
        for produto in estoque_produtos:

            if produto["nome"].lower() == nome_produto.lower():

                # Atualiza a quantidade do produto no estoque
                produto["quantidade"] += quantidade_entrada

                print("Quantidade atualizada com sucesso.")

                produto_encontrado = True

                break

        # Caso o produto não exista no estoque
        if not produto_encontrado:
            print("Produto não encontrado.")

    # Opção 3 - Registra a saída de produtos
    elif opcao_usuario == "3":

        nome_produto = input("Digite o nome do produto: ")

        # Converter o valor digitado de string para um número inteiro
        quantidade_saida = int(input("Digite a quantidade para saída: "))

        produto_encontrado = False

        # Percorre a lista procurando o produto informado
        for produto in estoque_produtos:

            if produto["nome"].lower() == nome_produto.lower():
                 
                 produto_encontrado = True

                 # Verifica se há quantidade suficiente em estoque
                 if produto["quantidade"] >= quantidade_saida:
                     
                     # Realiza a saída do produto
                     produto["quantidade"] -= quantidade_saida

                     print("Saída realizada com sucesso.")

                 else:
                     print("Estoque insuficiente")

                 break
        # Caso o produto não exista no estoque
        if not produto_encontrado:
            print("Produto não encontrado.") 

    # Opção 4 - Finalizar o sistema
    elif opcao_usuario == "4":

        print("Encerrando o sistema...")

        # Encerra o loop principal do programa
        break

    # Caso o usuário digite uma opção inválida
    else:

        print("Opção inválida. Tente novamente.")
