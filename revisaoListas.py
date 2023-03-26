galera=[]   #Criando a lista
dado=[]
totalmaior=totalmenor=0
for cont in range(0,3):  #colocando a quantidade necessária de contagem
    dado.append(input('Nome: '))
    dado.append(int(input('Idade:')))
    galera.append(dado[:]) #salvando os dados
    dado.clear()
for p in galera: 
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totalmaior+=1
    else:
        print(f"{p[0]} é menor de idade")
        totalmenor+=1
print(F'Temos {totalmaior} maiores de idade e {totalmenor} menores de idade')