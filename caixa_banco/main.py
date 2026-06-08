print("="*25)
print("| BANCO CAIXA ECONÔMICO ")
print("="*25)

deposit25 = 0
deposit10 = 0
deposit5 = 0
deposit2 = 0

for i in range(4):
    if i == 0:
        deposit25 = int(input("Digite quanto de NOTAS de R$ 25,00 o caixa possui: --> "))
        deposit25tot = deposit25 * 25
    elif i == 1:
        deposit10 = int(input("Digite quanto de NOTAS de R$ 10,00 o caixa possui: --> "))
        deposit10tot = deposit10 * 10
    elif i == 2:
        deposit5 = int(input("Digite quanto de NOTAS de R$ 5,00 o caixa possui: --> "))
        deposit5tot = deposit5 * 5
    else:
        deposit2 = int(input("Digite quanto de NOTAS de R$ 2,00 o caixa possui: --> "))
        deposit2tot = deposit2 * 2
        
totalcaixa = deposit25tot + deposit10tot + deposit5tot + deposit2tot
        
print("+"*50)
print("| ----> DINHEIRO DISPONIVEL <----|")
print(f"| - R$ 25,00 - [{deposit25}]  ---- NOTAS|")
print(f"| - R$ 10,00 - [{deposit10}]  ---- NOTAS|")
print(f"| - R$ 5,00  - [{deposit5}] ---- NOTAS|")
print(f"| - R$ 2,00  - [{deposit2}]  ---- NOTAS|")
print("+"*50)

money = float(input("Digite a quantidade de Dinheiro que desejas Sacar --> "))

cont25 = 0
cont10 = 0
cont5 = 0
cont2 = 0

while money > totalcaixa:
   print("| Valor do CAIXA é menor do que o que vai ser sacado !!! Digite outro valor para PROSSEGUIR !!!")
   money = float(input("Digite a quantidade de Dinheiro que desejas Sacar --> "))
   
while money != 0:
    if deposit25 > 0 and money >= 25:
       money = money - 25
       deposit25-=1
       cont25+=1
    elif deposit10 > 0 and money >= 10:
         money = money - 10
         deposit10-=1
         cont10+=1
    elif deposit5 > 0 and money >= 5:
         money = money - 5
         deposit5-=1
         cont5+=1
    elif deposit2 > 0 and money >= 2:
         money = money - 2
         deposit2-=1
         cont2+=1
    
print(f"|Voce recebeu {cont25} em notas de R$ 25,00 |")
print(f"|Voce recebeu {cont10} em notas de R$ 10,00 |")
print(f"|Voce recebeu {cont5} em notas de R$ 5,00  |")
print(f"|Voce recebeu {cont2} em notas de R$ 2,00  |")

print("+"*50)
print("| ----> DINHEIRO DISPONIVEL <----|")
print(f"| - R$ 25,00 - [{deposit25}]  ---- NOTAS|")
print(f"| - R$ 10,00 - [{deposit10}]  ---- NOTAS|")
print(f"| - R$ 5,00  - [{deposit5}]  ---- NOTAS|")
print(f"| - R$ 2,00  - [{deposit2}]  ---- NOTAS|")
print("+"*50)
