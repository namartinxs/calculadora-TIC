def calculadora():
    while True:
        print("calculadora simples \n")
        print("1.soma\n2.Subtração\n3.Multiplicação\n4.Divisão\n5.Sair")
        operacao = input("Selecione uma opção ou 'S' para sair:")
        operacao = operacao.lower()
        opcoes = ['1', '2', '3', '4']
        if operacao == 's' or operacao == '5':
            print('Obrigada por utilizar meus serviços.')
            break

        if operacao not in opcoes:
            print('Opção invalída tente novamente')
            continue

        numero_1 = float(input("Primeiro número"))
        numero_2 = float(input("Segundo número"))

        if operacao == '1':
            resultado = numero_1 + numero_2
            op = 'soma'
            result = resultado
        elif operacao == '2':
            resultado = numero_1 - numero_2
            op = 'subtração'
            result = resultado
        elif operacao == '3':
            resultado = numero_1 * numero_2
            op = 'multiplicação'
            result = resultado
        else:
            if numero_2 == 0:
                print('Divisões por zero não são possíveis.')
                continue
            else:
                resultado = numero_1 / numero_2
                op = 'divisão'
                result = resultado

        result_msg = f'O resultado da operação {op} é {result}'
        print(result_msg)

calculadora()