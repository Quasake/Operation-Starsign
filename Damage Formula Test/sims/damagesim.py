import sys
sys.path.insert(1, '../')

import math
import plotly.graph_objects as go

from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()

    phys_attack = Attack('Physical Attack', 10, 1, 1)
    myst_attack = Attack('Mystical Attack', 10, 1, 0)

    test_count = 0
    total_tests = (math.factorial(len(characters)) / math.factorial(len(characters) - 2)) * 2

    print('Running tests...[Total tests : ' + str(total_tests) + ']')

    for a in range(len(characters)):
        for d in range(len(characters)):
            attacker = characters[a]
            defender = characters[d]

            if (attacker.name == 'God of the Seas' and defender.name == 'Tepunné Ceanna') or (defender.name == 'God of the Seas' and attacker.name == 'Tepunné Ceanna'):
                print_progress(test_count, total_tests, prefix='SKIP >', suffix='[' + attacker.name + ' > ' + defender.name + ']')

                test_count += 2
                continue

            if attacker.name != defender.name:
                print_progress(test_count, total_tests, prefix='PHYS >', suffix='[' + attacker.name + ' > ' + defender.name + ']')

                phys_trials = [phys_attack.calc_damage(attacker, defender) for i in range(2500)]
                phys_data = {attacker.name: phys_trials}

                fig = create_histogram(phys_data, attacker.name + ' Physical Attacks ' + defender.name, 'Damage')
                fig.write_image('../graphs/damagesim/' + attacker.name.replace(' ', '').lower() + '_pattack_' + defender.name.replace(' ', '').lower() + '.png')

                test_count += 1

                print_progress(test_count, total_tests, prefix='MYST >', suffix='[' + attacker.name + ' > ' + defender.name + ']')

                myst_trials = [myst_attack.calc_damage(attacker, defender) for i in range(2500)]
                myst_data = {attacker.name: myst_trials}

                fig = create_histogram(myst_data, attacker.name + ' Mystical Attacks ' + defender.name, 'Damage')
                fig.write_image('../graphs/damagesim/' + attacker.name.replace(' ', '').lower() + '_mattack_' + defender.name.replace(' ', '').lower() + '.png')

                test_count += 1

    print_progress(test_count, total_tests, prefix=' >', suffix='[Done!]')

if __name__ == '__main__':
    sim()
