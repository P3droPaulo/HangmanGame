from random import choice
from hang_draw import *

word_list = ['cacau', 'amora', 'caqui', 'limao', 'manga', 'melao', 'mamao']
draw_list = [hang, head, body, left_arm, right_arm, left_leg, full_body]

class HangmanGame():
    def __init__(self):
        self.word = choice(word_list)
        self.letters = ['', '', '', '', '']
        self.word_row = ['_', '_', '_', '_', '_']
        self.count = [0, True]
        self.win = False

        for letter in range(len(self.word)):
            self.letters[letter] = self.word[letter]
    
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
