import math
import plotly.graph_objects as go

from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()

    print('Running tests...')

    base_attack = Attack('Base Attack', 10, 1, 1)

    test_count = 0
    total_tests = math.factorial(len(characters)) / math.factorial(len(characters) - 2)

    print_progress_bar(test_count, total_tests, prefix='>')

    for a in range(len(characters)):
        for d in range(len(characters)):
            attacker = characters[a]
            defender = characters[d]

            if attacker.name != defender.name:
                test_count += 1
                print_progress_bar(test_count, total_tests, prefix='>', suffix='[' + attacker.name + ' Attacks ' + defender.name + ']' + (' ' * 15))

                trials = [base_attack.calc_damage(attacker, defender) for i in range(2500)]

                fig = go.Figure(data=go.Histogram(x=trials, nbinsx=100))
                fig.update_layout(title=attacker.name + ' Attacks ' + defender.name, xaxis_title='Damage', yaxis_title='Number of Times')

                fig.write_image('graphs/damagesim/' + attacker.name.replace(' ', '').lower() + '_attacks_' + defender.name.replace(' ', '').lower() + '.png')

    print('Done!')

if __name__ == '__main__':
    sim()
