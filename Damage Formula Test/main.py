import numpy as np
import plotly.graph_objects as go

from character import Character
from attack import Attack

characters = []
test_count = 0
loading_count = 0
total_tests = 182

characters.append(Character('Tepunne',  20, 15, 5,  16, 17, 24, 10, 15, 10, 10))
characters.append(Character('Aloro',    30, 30, 9,  24, 10, 28, 5,  35, 5,  8))
characters.append(Character('Anabelle', 13, 10, 10, 12, 14, 12, 19, 26, 10, 5))
characters.append(Character('Barthon',  10, 14, 4,  8,  0,  10, 13, 15, 26, 40))
characters.append(Character('Ellie',    11, 13, 3,  10, 30, 12, 20, 20, 13, 25))
characters.append(Character('Farella',  50, 20, 2,  20, 17, 36, 9,  11, 10, 10))
characters.append(Character('Haest',    16, 8,  13, 13, 10, 20, 11, 23, 30, 13))
characters.append(Character('Lytra',    15, 17, 3,  13, 21, 18, 10, 14, 10, 10))
characters.append(Character('Mietra',   17, 15, 4,  12, 26, 24, 12, 17, 10, 10))
characters.append(Character('Roy',      10, 0,  6,  12, 0,  6,  12, 45, 40, 20))
characters.append(Character('Egge',     0,  45, 8,  12, 30, 18, 15, -1, 8,  8))
characters.append(Character('Taroh',    26, 15, 15, 35, 14, 36, 3,  9,  5,  10))
characters.append(Character('Twins',    6,  5,  6,  2,  13, 2,  30, 38, 25, 15))
characters.append(Character('GOTS',     20, 15, 10, 8,  34, 12, 20, 23, 15, 10))

base_attack = Attack('Base Attack', 10, 1, 1)

# print(base_attack.calc_damage(characters[0], characters[2]))

'''
trials = [base_attack.calc_damage(characters[0], characters[2]) for i in range(2500)]
fig = go.Figure(data=go.Histogram(x=trials, nbinsx=100))
fig.show()
'''

def print_progress_bar (iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', print_end="\r"):
    """
    WEBSITE: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console

    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        print_end   - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)

    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = print_end)

    # Print New Line on Complete
    if iteration == total:
        print()

print('Running tests...')

for a in range(len(characters)):
    for d in range(len(characters)):
        attacker = characters[a]
        defender = characters[d]
        
        if attacker.name != defender.name:
            test_count += 1
            print_progress_bar(test_count, total_tests, prefix=' Progress : ', length=50)
            
            trials = [base_attack.calc_damage(attacker, defender) for i in range(2500)]

            fig = go.Figure(data=go.Histogram(x=trials, nbinsx=100))
            fig.write_image('graphs/' + attacker.name + '_attacks_' + defender.name + '.png')

print('\nDone!')
