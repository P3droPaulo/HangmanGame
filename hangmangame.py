from random import choice
from hang_draw import *

fruit_list = ['cacau', 'amora', 'caqui', 'limao', 'manga', 'melao',
             'mamao', 'abacaxi', 'jabuticaba', 'melancia', 'banana',
             'morango', 'laranja', 'pera', 'goiaba', 'lichia', 'jaca',
             'framboesa', 'cereja', 'kiwi', 'acerola', 'caju', 'guarana'
             'tangerina', 'tomate', 'roma', 'pitaia', 'ameixa', 'pessego',
             'uva', 'damasco', 'pitanga']

animal_list = ['cachorro', 'gato', 'papagaio', 'pato', 'elefante', 'formiga',
                'cobra', 'aranha', 'jacare', 'girafa', 'alce', 'urso', 'arara',
                'veado', 'peixe', 'baleia', 'tubarao', 'foca', 'lagosta', 'camarao',
                'cavalo', 'vaca', 'tigre', 'leao', 'bufalo', 'rinoceronte', ' hipopotomo',
                'borboleta', 'lagarta', 'lagartixa', 'calango', 'macaco', 'gorila', 'guaxinim',
                'tartaruga', 'barata', 'galinha', 'morcego', 'aguigita', 'caranguejo', 'polvo']

draw_list = [hang, head, body, left_arm, right_arm, left_leg, full_body]

class HangmanGame():
    def __init__(self):
        self.word = choice(animal_list)
        self.letters = []
        self.word_row = []
        self.count = [0, True]
        self.win = False

        for letter in range(len(self.word)):
            self.letters.append(self.word[letter])
            self.word_row.append('_')
    
    def draw(self):
        return draw_list[self.count[0]]
    
    def word_verify(self, letter_input):
        for letter in range(len(self.letters)):
            if letter_input == self.letters[letter]:
                self.word_row[letter] = letter_input
                

        if letter_input not in self.letters and self.count[0] <= 6:
            self.count[0] += 1

        if self.count[0] == 6:
            self.count[1] = False
        
        elif self.word_row == self.letters:
            self.win = True