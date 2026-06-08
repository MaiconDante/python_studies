import time
import random as rd

def validation(num, op=0):
  if num:
    while len(num) != 1 or num.isdigit() == False or (num < "1" or num > "8"):
      num = input("\n|Número digitado INVÁLIDO !!! Favor digitar novamente|: --> ")
    return num
  else:
    while len(op) != 1 or op.isdigit() == False or (op < "0" or op > "3"):
      op = input("\n|Opção digitada INVÁLIDA !!! Favor digitar novamente|: --> ")
    return op

print(">"*33)
print("|------> QUIZ DE PYTHON <-------|")
print("<"*33)

qtd = input("\nDigite a quantidade de Perguntas que desejas Responder: |De 1 a 8| --> ")
qtd_answer = validation(qtd)

time.sleep(1)
print("Prepara-se vamos COMEÇAR !!!")
time.sleep(2)
print("[Iniciado]")

answers = [
      {
          "Pergunta":"Qual palavra usada para criação de função em python ?",
          "Opções":["def","fx","function()","func()"],
          "Resposta":"0",
      },
       {
          "Pergunta":"Quem é o criador do Python ?",
          "Opções":["Stephen George","Guido Van Rossum","Steven Jobs","Ralf Stuart"],
          "Resposta":"1",
      },
      {
          "Pergunta":"Qual é a estrutura de LISTAS em python ?",
          "Opções":["lista = (1,2,3,4)","lista = [1,2,3,4]","lista = list()","Opção 1 e 2 estão Corretas"],
          "Resposta":"3",
      },
       {
          "Pergunta":"Veja esta estrutura de variáveis | var = '1' || new_var = 2 |, o que acontece se fizermos var + new_var ?",
          "Opções":["12","3","error","112"],
          "Resposta":"1",
      },
      {
          "Pergunta":"| var = 5 < 6 | Que tipo de Váriavel é o var mencionado ?",
          "Opções":["int","str","bool","float"],
          "Resposta":"2",
      },
       {
          "Pergunta":"Quais são os comandos de laço de repetição ?",
          "Opções":["While","If Else","For","Opção 0 e 2 estão Corretas"],
          "Resposta":"3",
      },
      {
          "Pergunta":"If-Elif-Else são comandos de laço .... ?",
          "Opções":["Repetição","Constantes","Condicional","Negação"],
          "Resposta":"2",
      },
       {
          "Pergunta":"Qual comando para instalar pacotes/bibliotecas no Python ?",
          "Opções":["pip install","install package","install apt get","import install"],
          "Resposta":"0",
      },
               ]

correct = 0

for i in range(int(qtd_answer)):
  choice = rd.randint(0, 7)
  time.sleep(2)
  print(f"\nPERGUNTA:[{i+1}]->",answers[choice]["Pergunta"])
  print("OPÇÕES: ")
  for o in range(len(answers[choice]["Opções"])):
    print(f"{o}) -",answers[choice]["Opções"][o])
  resp = input("Digite a opção correspondente a sua resposta --> R: ")
  option = validation(0, resp)
  if answers[choice]["Pergunta"][choice]:
    if resp == answers[choice]["Resposta"][0]:
      print("\n|VOCÊ < ACERTOU > !!! [PARABÉNS] !!!|")
      correct += 1
    else:
      print("\n|VOCÊ < ERROU > !!! TENTE NA PRÓXIMA VEZ !!!|")

print("\n")
print("="*56)
print(f"Você ACERTOU {correct} Perguntas de uma série de {qtd_answer} Perguntas !!!")
print("="*56)
