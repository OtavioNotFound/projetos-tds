o = ""

while o != "0":
    print("\n1 - Ver se é par ou ímpar")
    print("2 - Contador com intervalo")
    print("3 - Somar números até parar")
    print("0 - Sair")

    o = input("\nEscolha uma opção: ")

    if o == "1":
        while True:
            e = input("\nDigite um número (ou 'sair'): ")
            if e.lower() == 'sair':
                break

            if e.replace('-', '', 1).isdigit():
                n = int(e)
                r = "Par" if n % 2 == 0 else "Ímpar"
                print("O número", n, "é", r)
            else:
                print("Erro: Digite um número inteiro válido.")

    elif o == "2":
        a = int(input("Começa em: "))
        b = int(input("Termina em: "))
        p = int(input("Pular de quanto em quanto: "))

        print("Contando...")
        for i in range(a, b + 1, p):
            print(i, end=" ")
        print("\nFim da contagem.")

    elif o == "3":
        s = 0
        c = 0
        while True:
            v = float(input("Digite um valor (0 para parar): "))
            if v == 0:
                break
            s += v
            c += 1

        if c > 0:
            print("Total de números digitados:", c)
            print("Soma de tudo:", s)
        else:
            print("Nenhum número foi digitado.")

    elif o == "0":
        print("Saindo do programa...")
        
    else:
        print("Opção inválida, tente novamente.")
