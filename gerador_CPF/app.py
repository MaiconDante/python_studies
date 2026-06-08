# IMPORTANDO BIBLIOTECA
import random

def primary_digit(qtd_cpf):
  # CÁLCULO DO PRIMEIRO DÍGITO DO CPF !!!
  for _ in range(int(qtd_cpf)):

    global cpf_nine_digit
    cpf_nine_digit = ""

    for i in range(9):
      cpf_nine_digit += str(random.randint(0, 9))
    totalizer = 0

    for i, value in enumerate(cpf_nine_digit,-10):
      totalizer += abs((i * int(value)))

    calc_first_digit = (totalizer * 10) % 11

    if calc_first_digit > 9:
      return 0
    else:
      return calc_first_digit

def second_digit():
  # CÁLCULO DO SEGUNDO DÍGITO DO CPF !!!

  global cpf_eleven_digit
  cpf_eleven_digit = cpf_nine_digit+str(primary_digit())
  totalizer_2 = 0

  for i, value in enumerate(cpf_eleven_digit,-11):
    totalizer_2 += abs((i * int(value)))

  calc_second_digit = (totalizer_2 * 10) % 11

  if calc_second_digit > 9:
    return 0
  else:
    return calc_second_digit


if __name__ == "__main__":
  qtd_cpf = input("Digite a quantidade de CPF'S que gostaria que fosse gerado: ")

  while qtd_cpf.isdigit() == False:
    qtd_cpf = input("Isso não é um número, digite apenas números: ")

  new_cpf = cpf_eleven_digit+str(second_digit())
  mask = new_cpf[:3]+"."+new_cpf[3:6]+"."+new_cpf[6:9]+"-"+new_cpf[9:11]
  print(">"*17)
  print("|   CPF GERADO  |")
  print("|---------------|")
  print(f"|{mask} |")
  print("|---------------|")
  print("<"*17)