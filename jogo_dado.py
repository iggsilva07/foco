from random import randint
from time import sleep
from operator import itemgetter
ranking = list()
painel = ['>>>>> Dados sorteados <<<<<<', '>>>>> Classificações <<<<<<', '>>>>>>FIM DE JOGO<<<<<<<']

jogo = {'jogador1': randint(1, 6),
        'jogador2': randint(1, 6),
        'jogador3': randint(1, 6),
        'jogador4': randint(1, 6)}
print('-'*len(painel[0]))
print(f'{painel[0]}')
print('-'*len(painel[0]))
for k, v in jogo.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-'*len(painel[1]))
print(f'{painel[1]}')
print('-'*len(painel[1]))
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'O{i+1}º lugar {v[0]} com {v[1]}. ')
    sleep(1)
print('-'*len(painel[2]))
print(f'{painel[2]}')
print('-'*len(painel[2]))
