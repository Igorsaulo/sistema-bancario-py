from caixa import Caixa


caixa = Caixa()
while True:
    print('1 - Depositar')
    print('2 - Sacar')
    print('3 - Extrato')
    print('4 - Sair')
    opcao = input('Digite a opcao desejada: ')
    if(opcao == '1'):
        valor = input('Digite o valor a ser depositado: ')
        caixa.depositar(valor)
    elif(opcao == '2'):
        valor = input('Digite o valor a ser sacado: ')
        caixa.sacar(valor)
    elif(opcao == '3'):
        caixa.exibir_extrato()
    elif(opcao == '4'):
        break
    else:
        print('Opcao invalida!')
    print('------------------------')
    
print('Fim do programa!')