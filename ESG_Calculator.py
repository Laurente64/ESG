# Definindo a função menu(), dizendo o que ela vai fazer
def menu():
    print("""\n+=+= Calculadora +=+=

0 - Sair;
1 - Adição;
2 - Subtração;
3 - Multiplicação;
4 - Divisão.""")
 
    # Escolhendo a ação da calculadora
    escolha = int(input(("Digite a sua escolha: ")))
    return escolha
 
while True:
 
    # Executando, chamando, a função menu(), que mostra o menu e retorna o número da escolha
    escolha = menu()
 
    # Se a variável escolha tiver o valor de 0, o programa vai encerrar
    if escolha == 0:
        break
   
    # Definindo quantos números vão estar na operação, e definindo que o valor é um número inteiro (não é decimal, não tem vírgula)
    else:
        qnt = int(input("Quantas vezes números serão selecionados: "))

        # Caso a operação escolhida for adição
        if escolha == 1:
            # Inciando uma váriavel para guardar o resultado
            resultado = 0

            # Repete a quantidade de números solicitados para a soma
            for i in range(qnt):
                # Recebe o número que deve ser somado
                num = float(input(f"Digite o valor do {i+1}° número: "))

                # Acrescenta esse número na variável
                resultado += num

            # Mostrando o resultado da operação
            print(f"O resultado da soma é {resultado}")

        # Caso a operação escolhida for subtração
        elif escolha == 2:
            # Recebe o primeiro número da subtração
            num = float(input(f"Digite o valor do {1}° número: "))

            # Adiciona o número na variável resultado
            resultado = num

            # Repete a quantidade de números que devem ter na operação (qnt - 1, porque é a quantidade menos o primeiro número)
            for i in range(qnt - 1):
                # Recebe o próximo número da operação (mostrado i + 2, porque o i começa em zero e estamos varrendo a partir do segundo número)
                num = float(input(f"Digite o valor do {i + 2}° número: "))

                # Descrescendo da variável resultado
                resultado -= num

            # Mostrando o resultado da operação
            print(f"O resultado da subtração é {resultado}")
 
        # Caso a operação escolhida for multiplicação
        elif escolha == 3:
            # Criando uma variável para guardar o resultado que não tem valor (None é um valor vazio)
            resultado = None

            for i in range(qnt):
                # Pergunta o valor do próximo número (é i + 1, já que i começa no 0)
                num = float(input(f"Digite o valor do {i + 1} número: "))

                # Caso o primeiro número ainda não tenha sido lido
                if resultado != None:
                    # Multiplicando o número lido pelo resultado e substituindo com o novo valor
                    resultado *= num

                # Atribuindo o primeiro número lido, para pode realizar a multiplicação com um valor válido
                else:
                    resultado = num

            # Mostrando o resultado da operação
            print(f"O resultado da multiplicação é {resultado}")
 
        # Caso a operação escolhida for divisão
        elif escolha == 4:
            # Criando uma variável para guardar o resultado que não tem valor (None é um valor vazio)
            resultado = None

            for i in range(qnt):
                # Pergunta o valor do próximo número (é i + 1, já que i começa no 0)
                num = float(input(f"Digite o valor do {i + 1} número: "))

                # Caso o primeiro número ainda não tenha sido lido
                if resultado != None:
                    # Dividindo o número lido pelo resultado e substituindo com o novo valor
                    resultado /= num

                # Atribuindo o primeiro número lido, para pode realizar a divisão com um valor válido
                else:
                    resultado = num

            # Mostrando o resultado da operação
            print(f"O resultado da multiplicação é {resultado}")
 
        # Caso a operação escolhida for inválida, o usuário será informado sobre o erro
        else:
            print("Opção inválida!")