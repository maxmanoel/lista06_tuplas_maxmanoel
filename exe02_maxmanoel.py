#EXE 002 - Faça um programa que o usuario insira 10 produtos numa tupla. Exiba todos os produtos, 
# solicite ao usuário para digitar um nome de produto e exiba a posição dele, em seguida peça para digitar numero entre 0 e 9 e exiba o produto da tupla.

produto = ["Aplle","Samsung", "Xiami", "Redmi", 'Radio', "JBL som","Geladeira", "Forno eletrico", "Fogão", "Munitor"]
produto_eletronicos = input("Dgite o nome do produto (Aplle, Samsung, Xiami, Redmi,Radio, JBL som, Geladeira, Forno eletrico, Fogão, Munitor: ")
if produto_eletronicos in produto:
    posicao = produto.index(produto_eletronicos)

    print(f"O produto {produto_eletronicos} esta na posicao {posicao} da lista.")

    
    numero = int(input("Digite um numero entre 0 a 9: "))

    if 0<= numero < len(produto):
         
        print(f"O numero {numero} esta na posicao {produto[numero]} da lista.")

        
    print("MAX MANOEL")

else:   
        print("O produto digitado nao esta na lista.")
        print("MAX MANOEL")
        