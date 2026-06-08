import random as rd
board = ["_"] * 9
x = "X"
o = "O"

def validationjog(op):
    while board[op] != "_":
        op = int(input("Este campo já tem um valor, escolha outro campo: -->" ))
    board[op] = x
    if (board[0] == board[1] == board[2] != "_") or (board[3] == board[4] == board[5] != "_") or \
       (board[6] == board[7] == board[8] != "_") or (board[0] == board[3] == board[6] != "_") or \
       (board[1] == board[4] == board[7] != "_") or (board[2] == board[5] == board[8] != "_") or \
       (board[0] == board[4] == board[8] != "_") or (board[2] == board[4] == board[6] != "_"):
        return True
    return False

def validationia(op):
    while board[op] != "_":
        op = rd.randint(0, 8)
    board[op] = o
    if (board[0] == board[1] == board[2] != "_") or (board[3] == board[4] == board[5] != "_") or \
       (board[6] == board[7] == board[8] != "_") or (board[0] == board[3] == board[6] != "_") or \
       (board[1] == board[4] == board[7] != "_") or (board[2] == board[5] == board[8] != "_") or \
       (board[0] == board[4] == board[8] != "_") or (board[2] == board[4] == board[6] != "_"):
        return True
    return False

while True:
    print("+"*50)
    print(">>>>>>>>>>>>>>>   JOGO DA VELHA   <<<<<<<<<<<<<<<")
    print("+"*50)
    print("""
    -- CONFORME COORDENADAS NO QUADRO A SEGUIR ESCOLHA O NÚMERO CORRESPONDENTE AO LOCAL DE ONDE COLOCARÁ SUA OPÇÃO --
                                         
    ['0'|'1'|'2']
    --------------
    ['3'|'4'|'5']
    --------------
    ['6'|'7'|'8']
    """)
    print("-"*115)
    
    for i in range(0, 9, 3):
        print(board[i:i+3])
    print("-"*115)

    jogador = int(input("Digite um número de 1 a 8 correspondente ao local: --> "))

    if validationjog(jogador):
        print("VOCÊ VENCEU !!!")
        break
    
    ia = rd.randint(0, 8)
    
    if validationia(ia):
        print("VOCÊ PERDEU !!!")
        break
    
    # Checar empate
    if "_" not in board:
        print("JOGO EMPATADO !!!")
        break
