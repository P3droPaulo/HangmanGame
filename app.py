from hangmangame import HangmanGame
from hang_draw import *
from os import system

while True:
    system('cls')
    print(header)
    print(menu)
    opc = input('>>> ')

    if opc.isdigit():
        if opc == '1':
            while True:
                hang = HangmanGame()
                while hang.count[1] and not hang.win:
                    system('cls')
                    print(header)

                    print('\033[33mAs palavras não possuem acentuação!\033[m')
                    draw(hang.draw())
                    print('Dica: Fruta')
                    write(hang.word_row)

                    print(f"\n{'='*(len(header))}")
                    hang.word_verify(input('>>> ').lower())

                if hang.win:
                    system('cls')
                    print(header)
                    print('\033[33mAs palavras não possuem acentuação!\033[m')

                    draw(hang.draw())
                    print(f'\033[32mParabens você venceu!\033[m\nVocê Venceu com {hang.count[0]} Erros.')

                    print(f"{'='*(len(header))}")

                else:
                    system('cls')
                    print(header)
                    print('\033[33mAs palavras não possuem acentuação!\033[m')

                    draw(hang.draw())
                    print(f'A Palavra era: {hang.word.title()}')

                    print(f"{'='*(len(header))}")
                
                break
        elif opc == '2':
            system('cls')
            input('Em Breve!\n')
