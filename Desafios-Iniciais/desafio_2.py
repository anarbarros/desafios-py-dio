#Entrada

#A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na competição.
#Saída

#Seu programa deve produzir uma única linha com um número racional representando o número médio de cachorros-quentes consumidos pelos participantes. O resultado deve ser escrito como um número racional com exatamente dois dígitos após o ponto decimal, arredondado se necessário.

valores = input().split() 

h = int(valores[0])
p = int(valores[1])
media = h / p
# 
#   Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais.
print('%.2f'%(media))