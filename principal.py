import funcoes as fn

print("Bem-vindo! ദ്ദി(˵ •̀ ᴗ - ˵ ) Trabalho Prático Prog II")

while True:
    print("\nMenu:")
    print("F - Frases")
    print("M - Matrizes")
    print("S - Sair")
    
    opcao= input("Escolha uma opção: ").upper()
    
    if opcao == "S":
        break
    
    elif opcao == "F":
        quantidade= int(input("Digite a quantidade de frases: "))
        frases= fn.array_frases(quantidade)
        print("Substantivos disponiveis:", fn.substantivos)
        termo= input("Digite um substantivo para buscar: ")
        fn.verifica_termo(frases, termo)
        for frase in frases:
            vogais, consoantes= fn.conta_vogais_consoantes(frase)
            print(frase, "Vogais:", vogais, "Consoantes:", consoantes)

    elif opcao == "M":
        inicio= int(input("Digite um valor inicial: "))
        fim= int(input("Agora um valor final: "))
        linhas= int(input("Quantidade de linhas: "))
        colunas= int(input("Quantidade de colunas: "))
        matriz_completa= fn.gera_matrix(linhas, colunas, inicio, fim)
        fn.imprime_matrix(matriz_completa)
        total, media= fn.soma_media_matriz(matriz_completa)
        print("Soma:", total, "Média:", media)
    
    else:
        print("Opção inválida!")


print("Até logo! (๑'ᵕ'๑)⸝*")
