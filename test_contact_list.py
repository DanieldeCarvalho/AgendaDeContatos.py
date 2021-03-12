dicionario = {
    'Daniel' : {
        'sobrenome': 'Carvalho',
        'idade': '18'
},
    'Maria' : {
        'sobrenome': 'Souza',
        'idade': '23'
}  ,  'João' : {
        'sobrenome': 'Lima',
        'idade': '19'
}
}


def ler_dados():
    nome = input('Digite seu nome: ')
    sobrenome = input('Digite sua sobrenome: ')
    idade = input('Digite sua idade')
    return nome, sobrenome, idade


def mostrar_contatos():
    for contato in dicionario:
        print(contato)
        # print(f'Nome: ',{dicionario[contato]},'\nidade: '{dicionario['contato']['idade']})

while True:
    print('1 - mostrar pessoas cadastradas')
    print('2 - adicionar contato')
    print('3 - remover contato')
    print('4 - sair do programa')
    opcao = input('Escolha uma opção: ')

    if opcao == '1':
        mostrar_contatos()

    elif opcao == '4':
        break

    else:
        break