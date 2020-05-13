vagas_onibus = list(range(1, 25))
def painel():
    print('='*57)


def pol():

    for poltronas in vagas_onibus:
        print(f'{[poltronas]}', end=' ')
        if poltronas == 13:
            print('\n')
    print()

painel()
pol()
painel()
name = str(input('Digite seu nome: ')).upper()
while True:
    esc = 'SN'
    num = int(input(f'Escolha uma poltrona de sua preferencia {name}! : '))
    vagas_onibus.insert(num, 'X')
    vagas_onibus.remove(num)


    painel()
    pol()
    painel()
    esc = str(input('Deseja continuar? ')).upper()
    painel()
    if esc == 'N':
        print(f'Obrigado {name} Volte sempre')
        painel()
        break
