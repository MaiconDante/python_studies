import os, sys

# Dicionário com carros e valores
carros = {
    "Marca": ["Chevrolet Tracker", "Chevrolet Onix", "Chevrolet Spin", "Hyundai HB20", "Hyundai Tucson", "Fiat Uno", "Fiat Mobi", "Fiat Pulse"],
    "Valores": [120, 90, 150, 85, 120, 60, 70, 130]
}

# Dicionário para armazenar carros alugados
carros_devolver = {
    "Marca": [],
    "Valores": []
}

def menu_inicial():
    while True:
        print("=== | Bem-vindo à Locadora de Carros | ===")
        print()
        print("-"*28)
        print("|0| - Consultar Portifólio |")
        print("|1| - Alugar um carro      |")
        print("|2| - Devolver um carro    |")
        print("|3| - Sair do Programa     |")
        print("-"*28)
        print("O que deseja realizar ?")
        opcao = input("Opção: -> ")

        while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 3:
            opcao = input("Opção digitada inválida, favor digitar somente as que aparecem no MENU de Opções: -> ")

        print()
        os.system("cls" if os.name == 'nt' else 'clear')

        if opcao == "3":
            print("Saindo do programa...")
            break

        if opcao == "0":
            consultar_portfolio()

        if opcao == "1":
            alugar_carro()

        if opcao == "2":
            devolver_carro()

def consultar_portfolio():
    print("=== | Portifólio de Carros | ===")
    print("-"*32)
    for i in range(0, len(carros["Marca"])):
        print(f"|{i}| {carros['Marca'][i]} - R$ {carros['Valores'][i]}")
    print()
    print("Escolha |0| para SAIR e |1| para CONTINUAR ?")
    opcao = input("Opção: -> ")
    while not opcao.isdigit() or int(opcao) < 0 or int(opcao) > 1:
        opcao = input("Opção inválida, digite |0| para SAIR ou |1| para CONTINUAR: -> ")
    print()
    if opcao == "0":
        sys.exit()
    else:
        menu_inicial()

def alugar_carro():
    print("=== | ALUGAR Carros | ===")
    print("-"*32)
    for i in range(0, len(carros["Marca"])):
        print(f"|{i}| {carros['Marca'][i]} - R$ {carros['Valores'][i]}")
    print("-"*32)
    print()
    print("Escolha o código referente ao carro desejado: ")
    escolha_carro = input("Opção: -> ")

    # Validação para garantir que a escolha seja um número válido dentro da lista de carros
    while not escolha_carro.isdigit() or int(escolha_carro) < 0 or int(escolha_carro) >= len(carros["Marca"]):
        escolha_carro = input(f"Opção inválida, por favor escolha um número entre 0 e {len(carros['Marca'])-1}: -> ")

    escolha_carro = int(escolha_carro)

    print("Escolha por quantos dias deseja alugar: ")
    escolha_dias = input("Opção: -> ")

    # Validação para garantir que o número de dias seja um valor positivo
    while not escolha_dias.isdigit() or int(escolha_dias) <= 0:
        escolha_dias = input("Opção inválida, digite um número de dias válido (maior que 0): -> ")

    escolha_dias = int(escolha_dias)
    print()
    os.system("cls" if os.name == 'nt' else 'clear')
    print(f"Você escolheu {carros['Marca'][escolha_carro]} por {escolha_dias} dia(s)")
    print(f"O Aluguel totalizaria R$ {carros['Valores'][escolha_carro] * escolha_dias}. Deseja Alugar? ")
    print("0 - SIM | 1 - NÃO")
    resposta = input("Opção: -> ")
    print("="*20)
    # Validação para garantir que a resposta seja válida
    while resposta not in ["0", "1"]:
        resposta = input("Opção inválida. Digite 0 para SIM ou 1 para NÃO: -> ")
    if resposta == "0":
        print("-"*50)
        print(f"Parabéns você alugou o {carros['Marca'][escolha_carro]} por {escolha_dias} dia(s)")
        print("-"*50)

        # Adiciona o carro alugado ao dicionário de carros devolvidos
        carros_devolver['Marca'].append(carros['Marca'][escolha_carro])
        carros_devolver['Valores'].append(carros['Valores'][escolha_carro])

        # Remover o carro escolhido das listas 'Marca' e 'Valores'
        del carros['Marca'][escolha_carro]
        del carros['Valores'][escolha_carro]

    else:
        print("-"*50)
        print("O carro não foi alugado. Voltando ao menu principal.")
        print("-"*50)

def devolver_carro():
    print("=== | DEVOLVER Carros | ===")
    print("-"*32)
    print()
    print("Segue a lista de carros alugados. Qual você deseja devolver: ")

    if len(carros_devolver["Marca"]) > 0:
        # Exibe a lista de carros alugados que estão em carros_devolver
        print("-"*32)
        for i in range(len(carros_devolver["Marca"])):
            print(f"|{i}| {carros_devolver['Marca'][i]} - R$ {carros_devolver['Valores'][i]}")
        print("-"*32)

        print("Escolha o código do carro que deseja devolver: ")
        devolver_carro = input("Opção: -> ")
        # Validação para garantir que a escolha seja um número válido dentro da lista de carros alugados
        while not devolver_carro.isdigit() or int(devolver_carro) < 0 or int(devolver_carro) >= len(carros_devolver["Marca"]):
            devolver_carro = input(f"Opção inválida, por favor escolha um número entre 0 e {len(carros_devolver['Marca'])-1}: -> ")
        print()
        os.system("cls" if os.name == 'nt' else 'clear')

        print("="*60)
        devolver_carro = int(devolver_carro)
        print(f"Obrigado por devolver o carro: | {carros_devolver['Marca'][devolver_carro]} |")
        print("="*60)
        os.system("cls" if os.name == 'nt' else 'clear')

        # Adiciona o carro devolvido de volta ao dicionário de carros disponíveis
        carros['Marca'].append(carros_devolver['Marca'][devolver_carro])
        carros['Valores'].append(carros_devolver['Valores'][devolver_carro])

        # Remove o carro devolvido da lista de carros alugados
        del carros_devolver['Marca'][devolver_carro]
        del carros_devolver['Valores'][devolver_carro]

    else:
        print("-"*50)
        print("Não há carros alugados para devolver. Voltando ao menu principal.")
        print("-"*50)
        print()

# Iniciar o menu
menu_inicial()