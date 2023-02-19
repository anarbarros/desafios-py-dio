valores = input().split()


tempo_gasto = int(valores[0])
velocidade_media = int(valores[1])
km = 12

litros = (velocidade_media / km) * tempo_gasto

print('%.3f'% (litros))