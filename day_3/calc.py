def calc():
    print("Calculadora do Davi\n########")
    choice = int(input("Digite:\n1 para soma\n2 para subtração\n3 para multiplicação: ")) 
    if choice <= 3:
        n1 = int(input("Digite um numero:"))
        n2 = int(input("Digite outro numero:"))
        if choice == 1:
            result = n1 + n2
        elif choice == 2:
            result = n1 - n2
        elif choice == 3:
            result = n1 * n2
    else:
        exit()
    return print(f"O resultado é:{result}")