import os

os.system("clear")

lista_compras = []

def adicionar_produto(nome, unidade, qtde, descricao): 
    produto = {  
        "Nome": nome,  
        "Unidade": unidade,  
        "Qtde": qtde,  
        "Descricão": descricao  
    } 
    lista_compras.append(produto)
    print()
    print("="*120)
    print("Produto adicionado com SUCESSO !!!")
    print("="*120)
    print()

def deletar_produto(id): 
    lista_compras.pop(id)
    print()
    print("="*120)
    print("Produto removido com SUCESSO !!!")
    print("="*120)
    print()

def pesquisar_produto(nome): 
    encontrados = [produto for produto in lista_compras if nome.lower() in produto["Nome"].lower()]
    if encontrados:
        total_quantidade = sum(float(produto["Qtde"]) for produto in encontrados)
        print("=" * 120)
        print(f"Produtos encontrados com o nome '{nome}':")
        for id, produto in enumerate(encontrados, start=1):
            print(f"{id}. Nome: {produto['Nome']}, Unidade: {produto['Unidade']}, "
                  f"Quantidade: {produto['Qtde']}, Descrição: {produto['Descricão']}")
        print("-" * 120)
        print(f"Quantidade total encontrada: {total_quantidade:.2f} {encontrados[0]['Unidade']} (aproximado).")
        print("=" * 120)
    else:
        print("=" * 120)
        print(f"Nenhum produto encontrado com o nome '{nome}'.")
        print("=" * 120)

while True:
    print("<"*120)
    print("------------------|LISTA DE COMPRAS|----------------------")
    print(">"*120)

    print("|>>>> Menu de Opções <<<<|")
    print("| 1 - Adicionar produto\n| 2 - Remover produto\n| 3 - Pesquisar produtos\n| 4 - Sair do programa\n")

    print("-"*120)
    if lista_compras:
        print("| ID | | PRODUTO |")
        for id, produto in enumerate(lista_compras):
            print(f"| {id} | | {lista_compras[id]} |")
    else:
        print("| LISTA DE COMPRAS VAZIA |")
    print("-"*120)

    opcao = input("Digite o número da opção escolhida: -> ")
    print()

    if opcao.isnumeric():
        valor = int(opcao)
        if valor >= 1 and valor <= 4:
            if valor == 4:
                print("\nObrigado por utilizar aplicativo [ Lista de Compras ]")
                break
            elif valor == 1:
                print("="*120)
                print("Adicione um produto a |LISTA DE COMPRAS|")
                print("="*120)
                nome = input("Digite o nome do produto: -> ")
                print("""\nAs opções de unidade:\nQuilograma\nGrama\nLitro\nMililitro\nUnidade\nMetro\nCentímetro\n""")
                unidade = input("Digite a unidade de medida do produto, conforme tabela acima: -> ")
                qtde = input("Digite a quantidade desejada do produto: -> ")
                descricao = input("Digite a descrição do produto: -> ")
                adicionar_produto(nome, unidade, qtde, descricao)
            elif valor == 2:
                print("="*120)
                print("Remova um produto da |LISTA DE COMPRAS|")
                print("="*120)
                id_delete = int(input("\nDigite aqui o ID do produto que desejas REMOVER: -> "))
                deletar_produto(id_delete)
            elif valor == 3:
                print("="*120)
                print("Pesquise um produto na |LISTA DE COMPRAS|")
                print("="*120)
                pesquisa_nome = input("\nDigite aqui o nome do produto que desejas PESQUISAR: -> ")
                pesquisar_produto(pesquisa_nome)
    else:
        print("-"*120)
        print("Atenção, digite apenas números e somente número referente ao |MENU DE OPÇÕES|")
        print("-"*120)
        continue

print("\nFim do Programa")
