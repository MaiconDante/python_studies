import random as rd

def apresentacao_matriz():
  return print("",matriz[0][0:4],"\n",matriz[1][0:4],"\n",matriz[2][0:4],"\n")

line1 = []
line2 = []
line3 = []
matriz = [line1, line2, line3]

for l in range(3):
  for c in range(3):
    if l == 0:
      line1.append(rd.randint(0,9))
    elif l == 1:
      line2.append(rd.randint(0,9))
    else:
      line3.append(rd.randint(0,9))

print("|MATRIZ GERADA|\n")
apresentacao_matriz()
