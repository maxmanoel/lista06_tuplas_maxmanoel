convidados = []
nome = input("Qual nome do convidado : ")
convidados.append(nome)
convite = input("Deseja convidar mais pessoas ? ")
i = convidados.index(nome)
while convite == 's':
    nome = input("Qual nome do convidado : ")
convidados.append(nome)
print(convidados, i ,"Foram convidados à festa.")
convite = input("Deseja convidar mais pessoas ? ")
else:
print(convidados)
pergunta = input("Digite o nome de um dos convidados : ")
print(pergunta, i )
pergunta2 = input("Você deseja que essa pessoa vá á festa?")
if pergunta2 == 'nao':
convidados.remove(pergunta)
print(convidados)