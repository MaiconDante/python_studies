print(">>>>>>>>>>>>>> VALIDADOR DE |CPF| <<<<<<<<<<<<<<")
print("\n")
cpf = input("Digite seu CPF (Apenas números e com 11 digitos): ")

while len(cpf) != 11 or cpf.isdigit() == False:
    cpf = input("CPF Inválido !!! Digite seu CPF (Apenas números e com 11 digitos): ")

# CÁLCULO DO PRIMEIRO DÍGITO DO CPF !!!

print("\n")
cpf_slice = cpf[:9]
totalizer = 0

for i, value in enumerate(cpf_slice,-10):
  print(f"{abs(i)} * {value} = {abs(i * int(value))}")
  totalizer += abs((i * int(value)))

print(f"\nTotal da SOMA é: [{totalizer}]")

calc_first_digit = (totalizer * 10) % 11

if calc_first_digit > 9:
  result = 0
  print(f"\nCáculo do primeiro Dígito é: {result}\n")
else:
  result = calc_first_digit
  print(f"\nCáculo do primeiro Dígito é: {result}\n")

# CÁLCULO DO SEGUNDO DÍGITO DO CPF !!!

print(">"*50)
print("\n")

cpf_slice_2 = cpf[:10]
totalizer_2 = 0

for i, value in enumerate(cpf_slice_2,-11):
  print(f"{abs(i)} * {value} = {abs(i * int(value))}")
  totalizer_2 += abs((i * int(value)))

print(f"\nTotal da SOMA é: [{totalizer_2}]")

calc_second_digit = (totalizer_2 * 10) % 11

if calc_second_digit > 9:
  result2 = 0
  print(f"\nCáculo do segundo Dígito é: {result2}\n")
else:
  result2 = calc_second_digit
  print(f"\nCáculo do segundo Dígito é: {result2}")

print("\n")
print(">"*50)

if cpf == cpf[:9]+str(result+result2) or cpf != cpf[0]*len(cpf):
  print("===========================")
  print("| CPF | Digitado é VÁLIDO |")
  print("===========================")
else:
  print("=============================")
  print("| CPF | Digitado é INVÁLIDO |")
  print("=============================")

print("<"*50)
