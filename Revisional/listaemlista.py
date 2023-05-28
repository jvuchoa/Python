totmaior=totmenor=0
galera=list()
dado=list()
for c in range(0,3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)
for p in galera:
    if p[1]>=18:
        print(f'{p[0]} é maior de idade.')
        totmaior+=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmenor+=1
print(f'Temos {totmaior} maiores de idade e {totmenor} menores de idade.')