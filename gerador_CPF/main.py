# Importando Biblioteca
import random

def obter_quantidade_cpf():
    qtd_cpf = input("Digite a quantidade de CPF'S que gostaria que seja gerado: ")

    while not qtd_cpf.isdigit():
        qtd_cpf = input("Isso não é um número, digite apenas números: ")

    return int(qtd_cpf)

def calcular_primeiro_digito(cpf_nove_digitos):
    totalizador = 0

    for i, valor in enumerate(cpf_nove_digitos, -10):
        totalizador += abs(i * int(valor))

    digito = (totalizador * 10) % 11

    return 0 if digito > 9 else digito

def calcular_segundo_digito(cpf_dez_digitos):
    totalizador = 0

    for i, valor in enumerate(cpf_dez_digitos, -11):
        totalizador += abs(i * int(valor))

    digito = (totalizador * 10) % 11

    return 0 if digito > 9 else digito

def gerar_cpf():
    cpf_nove_digitos = ""

    for _ in range(9):
        cpf_nove_digitos += str(random.randint(0, 9))

    primeiro_digito = calcular_primeiro_digito(cpf_nove_digitos)

    cpf_dez_digitos = cpf_nove_digitos + str(primeiro_digito)

    segundo_digito = calcular_segundo_digito(cpf_dez_digitos)

    return cpf_dez_digitos + str(segundo_digito)

def formatar_cpf(cpf):
    return (
        cpf[:3] + "." +
        cpf[3:6] + "." +
        cpf[6:9] + "-" +
        cpf[9:11]
    )

def exibir_cpf(cpf):
    print(">" * 17)
    print("|   CPF GERADO  |")
    print("|---------------|")
    print(f"| {formatar_cpf(cpf)} |")
    print("|---------------|")
    print("<" * 17)

def main():
    quantidade = obter_quantidade_cpf()

    for _ in range(quantidade):
        cpf = gerar_cpf()
        exibir_cpf(cpf)

if __name__ == "__main__":
    main()
    