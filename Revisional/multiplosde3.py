somaMultiplosde3=0
cont=0  #contador 
executar='sim'
while(executar=='sim'):
    numero=int(input('digite um número: '))
    if(numero%3==0):   #pedindo o resto da divisão com (%)
        cont+=1
        somaMultiplosde3=(somaMultiplosde3+numero)
    else:
        cont+=1
    executar=str.lower(input('outro valor? '))
print('soma dos múltiplos de 3:',somaMultiplosde3)