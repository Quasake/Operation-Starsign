import math
import plotly.graph_objects as go

from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()

    base_attack = Attack('Base Attack', 10, 1, 1)

    test_count = 0
    total_tests = math.factorial(len(characters)) / math.factorial(len(characters) - 2)

    print('Running tests...[Total tests : ' + str(total_tests) + ']')

    for a in range(len(characters)):
        for d in range(len(characters)):
            attacker = characters[a]
            defender = characters[d]

            if (attacker.name == 'God of the Seas' and defender.name == 'Tepunné Ceanna') or (defender.name == 'God of the Seas' and attacker.name == 'Tepunné Ceanna'):
                print_progress(test_count, total_tests, prefix='SKIP >', suffix='[' + attacker.name + ' >x< ' + defender.name + ']')

                test_count += 1
                continue

            if attacker.name != defender.name:
                print_progress(test_count, total_tests, prefix='ATTA >', suffix='[' + attacker.name + ' > ' + defender.name + ']')

                trials = [base_attack.calc_damage(attacker, defender) for i in range(2500)]

                fig = go.Figure(data=go.Histogram(x=trials, nbinsx=100))
                fig.update_layout(title=attacker.name + ' Attacks ' + defender.name, xaxis_title='Damage', yaxis_title='Number of Times')

                fig.write_image('graphs/damagesim/' + attacker.name.replace(' ', '').lower() + '_attacks_' + defender.name.replace(' ', '').lower() + '.png')

                test_count += 1

    print_progress(test_count, total_tests, prefix=' >', suffix='[Done!]')

if __name__ == '__main__':
    sim()
