def calculator():
    while True:
        print("Selecione a operação desejada: ")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Sair")

        choice = int(input("Digite a sua escolha (1/2/3/4/5): "))

        if choice == 5:
            break

        num1 = float(input("Digite o primeiro número: "))

        if choice == 1:
            result = num1 + (float(input("Digite o segundo número: ")))
            print("Resultado da adição:", result)
        elif choice == 2:
            result = num1 - 1(float(input("Digite o segundo número: ")))
            print("Resultado da subtração:", result)
        elif choice == 3:
            result = num1 * (float(input("Digite o segundo número: ")))
            print("Resultado da multiplicação:", result)
        elif choice == 4:
            result = num1 / (float(input("Digite o segundo número: ")))
            print("Resultado da divisão:", result)
        else:
            print("Operação inválida. Tente novamente.")

calculator()
