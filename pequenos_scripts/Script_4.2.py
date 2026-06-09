""" 
Supondo que a variável previsão tenha recebido a string
'It will be a sunny day today'
escreva instruções Python correspondentes a estas atribuições:

  
A variável cont, a quantidade de ocorrências da string 'day' na string previsão.
A variável clima, o índice em que a substring 'sunny' começa.
A variável troca, uma cópia de previsão na qual cada ocorrência da substring
'sunny' é substituída por 'cloudy'.
"""

previsao = 'It will be a sunny day today'

cont = previsao.count("day")

clima = previsao.index("sunny")
clima = previsao.find('sunny')

troca = previsao.replace('sunny', 'cloudy')



print(cont)
print(clima)
print(troca)

