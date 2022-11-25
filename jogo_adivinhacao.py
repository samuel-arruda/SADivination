from random import randint
from time import sleep
comp = randint(0, 10)

print('-' * 20, ' DESAFIO ', '-' * 20)
print('')
print("Eu pensei em um número entre 0 e 10, desafio você adivinhar!!!")
print('')
res = 0
gast = 0
cont = 5
while res != comp:

    res = int(input('Qual número eu pensei? '))

    if res == comp and cont == 5:
        sleep(2)
        print("\n PARABÉNS, ACERTOU  DE PRIMEIRA!")

    else:

        if res != comp and cont > 1:
            sleep(2)
            print('\n' * 2)
            print('=' * 10, ' Chance Nº{} '.format(cont), '=' * 10)
            print("\nVocê errou, tente de novo.")

        elif res != comp and cont == 1:
            print('\n')
            sleep(1)
            print('*' * 10, ' U L T I M A  C H A N C E ', '*' * 10)
            print("\nPENSE BEM !!!")

        elif res == comp and cont == 1:
            print("\n Você acertou, porem utilizou todas as suas chances!")

        elif res == comp and cont > 1:
            sleep(2)
            print("\nVocê acertou, mas gastou {} das suas cinco chances".format(gast))

        elif cont == 0:
            print('\n' * 10)
            print("Você gastou todas as suas chances!\n")
            print('-' * 10, " FIM DE JOGO!!! ", '-' * 10)
            sleep(2)
            res = comp

    cont -= 1
    gast += 1

    print('\n')

for c in range(1, 4):
    print('-')
    sleep(1)

print("=-" * 10, ' OBRIGADO POR JOGAR! ', '-=' * 10)





