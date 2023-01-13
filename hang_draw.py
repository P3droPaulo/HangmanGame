head = ['_____', '|   o ', '|', '|', '|']
body = ['_____', '|   o ', '|   |', '|', '|']
left_arm = ['_____', '|   o ', '|  /|', '|', '|']
right_arm = ['_____', '|   o ', '|  /|\ ', '|', '|']
left_leg = ['_____', '|   o ', '|  /|\ ', '|  /', '|']
full_body = ['_____', '|   o ', '|  /|\ ', '|  / \ ', '|']
hang = ['_____', '|', '|', '|', '|']


header = f"{'='*10} JOGO DA FORCA {'='*10}"

def draw(draw):
    for line in draw:
        print(line)

def write(text):
    for l in range(5):
        print(text[l].upper(), end='')