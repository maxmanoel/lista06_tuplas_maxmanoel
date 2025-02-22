#EXE 001 . - Crie uma tupla contendo os nomes de cinco países e exiba toda a tupla. 
#Peça ao usuário para inserir um dos países que foram mostrados a ele e, em seguida, exibir o número de índice (ou seja, posição na lista) desse item na tupla.


paises = ["brasil","Paraguai", "Argentina", "Japao"]
pais_inserido = input("Dgite o nome do pais(Brasil, Paraguai, Japao, Argentina: ")
if pais_inserido in paises:
    posicao = paises.index(pais_inserido)
    print(f"O pais {pais_inserido} esta na posicao {posicao} da lista.")
    print("MAX MANOEL")
else:
        print("O pais digitado nao esta na lista.")
        print("MAX MANOEL")