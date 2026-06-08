import random as rd
from os import system, name

def limpa_tela():
    # Se for windows
    if name == "nt":
        _ = system("cls")
    # Se for MAC
    else:
        _ = system("clear")

palavras_aleatorias = ["musica","python","vida","perfume","sistema"]
palavra_sorteada = rd.choice(palavras_aleatorias)
tamanho_palavra = len(palavra_sorteada)
letras_advinhadas = []
limite_jogada = 6
tentativas = 0
tabuleiro = ["""
         +--------+
         |        |
         |
         |
         |
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |
         |
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |        |
         |
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |       /|
         |
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |       /|\\
         |
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |       /|\\
         |       /
         |
         ===========
         """,
         """
         +--------+
         |        |
         |        0
         |       /|\\
         |       / \\
         |
         ===========
         """]

while tentativas < limite_jogada:
    if tentativas != 0:
        limpa_tela()
    print("="*50)
    print(">>>>>>>>>>>>>>>>>>>> HANGMAN <<<<<<<<<<<<<<<<<<<<")
    print("="*50)
    print(tabuleiro[tentativas])
    print("="*50)
    if tentativas == 0:
        print(f"A palavra secreta tem [{tamanho_palavra}] letras !!!")
        print(f"Você tem [{limite_jogada}] tentativas para acertar a palavra !!!")
    else:
        if resposta == 0:
         print(f"Letra digitada está |INCORRETA|") 
        else:
         print(f"Letra digitada está |CORRETA|")   
        print(f"Tentativas Restantes = [{limite_jogada-tentativas}]")
        
    print("="*50)   
    for letra in palavra_sorteada:
        if letra in letras_advinhadas:
            print(f"| {letra} |", end='')
        else:
            print(" |__|", end='')
        
    print("")
    print("="*50)
    
    letra_digitada = input("Digite uma letra para ver se advinha a palavra R -> ").strip().lower()[0]
    if letra_digitada in palavra_sorteada:
        letras_advinhadas.append(letra_digitada)
        resposta = 1
        if len(letras_advinhadas) == tamanho_palavra:
            break
    else:
        tentativas+=1 
        resposta = 0      
        
if tentativas < limite_jogada:
    print(">"*50)
    print(f"VOCÊ VENCEU A PALAVRA SORTEADA ERA: [{palavra_sorteada}]")
    print("<"*50)
else:
    print(">"*50)
    print(f"VOCÊ PERDEU !!! A PALAVRA ERA [{palavra_sorteada}]")
    print("<"*50)
    