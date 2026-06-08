palavra = input("Digite uma palavra para ser descoberta R: ").strip().lower()
qtd_palavra = len(palavra)
    
print(f"\nA palavra secreta contém {qtd_palavra} LETRAS !!!")
letra_acertada = ''
tentativas = 0

while True:
    letra_digitada = input("\nDigite uma letra !!! R: ").lower().strip()
    tentativas+=1
    print("\n")
    if len(letra_digitada) > 1:
        print("Digite apenas uma Letra !!!")
        continue
    
    if letra_digitada in palavra:
        letra_acertada += letra_digitada
        
    print("==================================")
    print("Palavra Formada: ", end="-> ")    
    
    for letra_secreta in palavra:
        if letra_secreta in letra_acertada:
            print(f"|{letra_secreta}|", end='')
        else:
            print("*", end='')
            
    if len(letra_acertada) == len(palavra):
        break

print("\n\n........................................................")    
print(f"VOCÊ VENCEU ACERTANDO A PALAVRA SECRETA QUE É: [{palavra}]")
print(f"VOCÊ FEZ ISSO EM: [{tentativas} tentativas]")
print("........................................................")
