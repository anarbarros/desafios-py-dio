# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input()) 

if ( salario <= 600 ):
  reajuste_ganho = salario + (salario * (17 / 100))
  novo_salario = salario + reajuste_ganho
  percentual = 17
  
  #print(f'''Novo salario: {novo_salario: .2f}
     #     Reajuste Ganho: {reajuste_ganho: .2f}
      #    Em percentual: 17%''' )

elif ( salario >= 600.01 and salario <=900.00 ):
  reajuste_ganho = salario + (salario * (13 / 100))
  novo_salario = salario + reajuste_ganho
  percentual = 13
  
 # print(f'''Novo salario: {novo_salario: .2f}
  #        Reajuste Ganho: {reajuste_ganho: .2f}
   #       Em percentual: 13%''' )
  
elif ( salario >=900.01 and salario <= 1500.00 ):
  reajuste_ganho = salario + (salario * (12 / 100))
  novo_salario = salario + reajuste_ganho
  percentual = 12
  
  #print(f'''Novo salario: {novo_salario: .2f}
          #Reajuste Ganho: {reajuste_ganho: .2f}
          #Em percentual: 12%''' )

elif ( salario >= 1500.01 and salario <= 2000.00 ):
  
  reajuste_ganho = salario + (salario * (10 / 100))
  novo_salario = salario + reajuste_ganho
  percentual = 10
  
#  print(f'''Novo salario: {novo_salario: .2f}
    #      Reajuste Ganho: {reajuste_ganho: .2f}
     #     Em percentual: 10%''' )

else: 
  reajuste_ganho = salario + (salario * (5 / 100))
  novo_salario = salario + reajuste_ganho
  percentual = 5
  
  #print(f'''Novo salario: {novo_salario: .2f}
     #     Reajuste Ganho: {reajuste_ganho: .2f}
   #       Em percentual: 5%''' )
   
print(f'Novo salario: {"{:.2f}".format(novo_salario)}\nReajuste ganho: {"{:.2f}".format(reajuste_ganho)}\nEm percentual: {percentual} %')
