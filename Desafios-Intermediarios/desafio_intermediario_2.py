while True: 
    try: 
        perna_levantada = input()
      
        if perna_levantada == 'esquerda':
            print('ingles')
        elif perna_levantada == 'direita':
            print('frances')
        elif perna_levantada == 'nenhuma':
            print('portugues')
        elif perna_levantada == 'ambas':
            print('caiu')
          # e imprima a saída de acordo com a situação das pernas do papagaio
    except EOFError: 
        break