import random
from art import tprint

contuser = 0
contpc = 0

while True:
  computador = random.randint(1, 3)
  try:
    print("-"*100)
    print("| JOGO DO PEDRA, PAPEL E TESOURA |")
    print()
    print("| CONFORME MENU | ESCOLHA UMA DAS OPÇÕES, SENDO:")
    print("1 - PAPEL ✋")
    print("2 - PEDRA ✊")
    print("3 - TESOURA ✌️")
    print("-"*100)
    print()
    tprint(f"PLACAR: {contuser} X {contpc}")
    print("-"*100)
    print()
    usuario = int(input("Digite a sua escolha: "))
    print()
    print("-"*100)
    while usuario < 1 or usuario > 3:
      print("="*100)
      print("Opção inválida. Escolha somente do 1 ao 3 !!!.")
      print("="*100)
      usuario = int(input("Digite a sua escolha: "))
      print()
      print("-"*100)

    print("+"*60)
    if usuario == 1 and computador == 1:
      print("JOGADOR: | PAPEL ✋ |  X  | PAPEL ✋ | COMPUTADOR")
      print("-"*100)
      print(" ---> EMPATE <--- ")
      print("-"*100)
      contuser += 1
      contpc += 1
    elif usuario == 2 and computador == 2:
      print("JOGADOR: | PEDRA ✊ |  X  | PEDRA ✊ | COMPUTADOR")
      print("-"*100)
      print(" ---> EMPATE <--- ")
      print("-"*100)
      contuser += 1
      contpc += 1
    elif usuario == 3 and computador == 3:
      print("JOGADOR: | TESOURA ✌️ |  X  | TESOURA ✌️ | COMPUTADOR")
      print("-"*100)
      print(" ---> EMPATE <--- ")
      print("-"*100)
      contuser += 1
      contpc += 1
    elif usuario == 1 and computador == 2:
      print("JOGADOR: | PAPEL ✋ |  X  | PEDRA ✊ | COMPUTADOR")
      print("-"*100)
      print(" ---> VOCÊ GANHOU <--- ")
      print("-"*100)
      contuser += 1
    elif usuario == 1 and computador == 3:
      print("JOGADOR: | PAPEL ✋ |  X  | TESOURA ✌️ | COMPUTADOR")
      print("-"*100)
      print(" ---> COMPUTADOR GANHOU <--- ")
      print("-"*100)
      contpc += 1
    elif usuario == 2 and computador == 1:
      print("JOGADOR: | PEDRA ✊ |  X  | PAPEL ✋ | COMPUTADOR")
      print("-"*100)
      print(" ---> COMPUTADOR GANHOU <--- ")
      print("-"*100)
      contpc += 1
    elif usuario == 2 and computador == 3:
      print("JOGADOR: | PEDRA ✊ |  X  | TESOURA ✌️ | COMPUTADOR")
      print("-"*100)
      print(" ---> VOCÊ GANHOU <--- ")
      print("-"*100)
      contuser += 1
    elif usuario == 3 and computador == 1:
      print("JOGADOR: | TESOURA ✌️ |  X  | PAPEL ✋ | COMPUTADOR")
      print("-"*100)
      print(" ---> VOCÊ GANHOU <--- ")
      print("-"*100)
      contuser += 1
    elif usuario == 3 and computador == 2:
      print("JOGADOR: | TESOURA ✌️ |  X  | PEDRA ✊ | COMPUTADOR")
      print("-"*100)
      print(" ---> COMPUTADOR GANHOU <--- ")
      print("-"*100)
      contpc += 1
    print("+"*60)

    tprint(f"PLACAR: {contuser} X {contpc}")
    repetir = input("Deseja jogar novamente? (S/N): ").strip().lower()
    while repetir not in ['s', 'n']:
      print("="*100)
      print("Opção inválida. Tente novamente.")
      print("="*100)
      repetir = input("Deseja jogar novamente? (S/N): ").strip().lower()
    if repetir == 's':
      continue
    else:
      print("\nObrigado por jogar! Até a próxima!")
      break

  except ValueError:
    print("="*100)
    print("Opção inválida. Tente novamente.")
    print("="*100)
    enter = input("Pressione Enter para continuar...")