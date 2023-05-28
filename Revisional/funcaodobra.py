def dobra(list):
    inicio=0
    while inicio<len(list):
        list[inicio]*=2
        inicio+=1


valores=[4,7,9,8,10,111,333]
dobra(valores)
print(valores)