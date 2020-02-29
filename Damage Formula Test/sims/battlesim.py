import sys
sys.path.insert(1, '../')

import math
import numpy as np
import plotly.graph_objects as go

from itertools import combinations_with_replacement
from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()
    combins = list(combinations_with_replacement(characters, 2))

    phys_average = []
    myst_average = []

    test_count = 0
    total_tests = (math.factorial(len(characters)) / (math.factorial(len(characters) - 2) * math.factorial(2))) * 2

    print('Running tests...[Total tests : ' + str(total_tests) + ']')

    for comb in combins:
        char_1 = comb[0]
        char_2 = comb[1]

        if (char_1.name == 'Barthon Vandera' and char_2.name == 'Roy Andrews') or (char_2.name == 'Barthon Vandera' and char_1.name == 'Roy Andrews'):
            print_progress(test_count, total_tests, prefix='SKIP >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            test_count += 2
            continue

        if (char_1.name == 'God of the Seas' and char_2.name == 'Tepunné Ceanna') or (char_2.name == 'God of the Seas' and char_1.name == 'Tepunné Ceanna'):
            print_progress(test_count, total_tests, prefix='SKIP >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            test_count += 2
            continue

        if char_1.name != char_2.name:
            print_progress(test_count, total_tests, prefix='PHYS >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            phys_trials = [battle_sim(char_1, char_2, PHYS_ATTACK) for i in range(2500)]

            phys_data = {char_1.name: [], char_2.name: []}
            for trial in phys_trials:
                phys_data[char_1.name if char_1.name == trial[1].name else char_2.name].append(trial[0])

            phys_average.extend(phys_data[char_1.name])
            phys_average.extend(phys_data[char_2.name])

            phys_fig = create_histogram(phys_data, char_1.name + ' Has Physical Battle With ' + char_2.name, 'Time to Kill [s]')
            phys_fig.write_image('../graphs/battlesim/' + char_1.name.replace(' ', '').lower() + '_pbattle_' + char_2.name.replace(' ', '').lower() + '.png')

            test_count += 1

            print_progress(test_count, total_tests, prefix='MYST >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            myst_trials = [battle_sim(char_1, char_2, MYST_ATTACK) for i in range(2500)]

            myst_data = {char_1.name: [], char_2.name: []}
            for trial in myst_trials:
                myst_data[char_1.name if char_1.name == trial[1].name else char_2.name].append(trial[0])

            myst_average.extend(myst_data[char_1.name])
            myst_average.extend(myst_data[char_2.name])

            myst_fig = create_histogram(myst_data, char_1.name + ' Has Mystical Battle With ' + char_2.name, 'Time to Kill [s]')
            myst_fig.write_image('../graphs/battlesim/' + char_1.name.replace(' ', '').lower() + '_mbattle_' + char_2.name.replace(' ', '').lower() + '.png')

            test_count += 1

    print_progress(test_count, total_tests, prefix=' >', suffix='[Done!]')

    print('Average Physical Battle Time : ' + str(average(phys_average)))
    print('Average Mystical Battle Time : ' + str(average(myst_average)))

if __name__ == '__main__':
    sim()
