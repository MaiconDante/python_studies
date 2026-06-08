def validation(val):
  if val:
    while len(val) != 1 or val.isdigit() == False or (val < "1" or val > "8"):
      val = input("\n|Número digitado INVÁLIDO !!! Favor digitar novamente|: --> ")
    return val

print("="*65)
height = input("Digite aqui um número de |1 a 8| para altura dos blocos --> ")

for i in range(int(height)+1):
    bloco = ("#"*i)
    print(bloco)

print("="*65)
   
for i in range((int(height)+1)):
    bloco = ("#"*i)
    print(f"{bloco:>{int(height)}}")
  
print("="*65)

# GERANDO BLOCOS NA MESMA LINHA

print("="*65)

height = input("Digite aqui um número de |1 a 8| para altura dos blocos --> ")

for i in range(int(height)+1):
    bloco = ("#"*i)
    print(f"{bloco:>{int(height)}}   {bloco}")

print("="*65)
