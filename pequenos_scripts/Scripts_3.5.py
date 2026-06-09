"""Implemente um programa que solicite do usuário uma lista de palavras
(ou seja, strings) e depois exiba na tela, uma por linha, todas as strings de
quatro letras nessa lista.

>>>
Digite a lista de palavras: ['pare', 'desktop', 'tio', 'pote']
pare pote"""

palavras = []

for i in range(4):
    dados = input("Digite uma palavra: -> ")
    while dados.isdigit() or dados == "":
        dados = input("Digite uma palavra ou letra, mas não números: -> ")
    palavras.append(dados)

print()
print("Palavras que contém apenas 4 letras são:")
for p in palavras:
    if len(p) == 4:
        print(p)


