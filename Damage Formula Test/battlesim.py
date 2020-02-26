import math
import plotly.graph_objects as go
import numpy as np

from itertools import combinations_with_replacement
from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()
    combins = list(combinations_with_replacement(characters, 2))

    phys_attack = Attack('Physical Attack', 10, 1, 1)
    myst_attack = Attack('Mystical Attack', 10, 1, 0)

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

            phys_trials = [do_battle(char_1, char_2, phys_attack) for i in range(250)]
            char_1_phys_trials = []
            char_2_phys_trials = []

            for trial in phys_trials:
                if char_1.name == trial[1].name:
                    char_1_phys_trials.append(trial[0])
                else:
                    char_2_phys_trials.append(trial[0])

            phys_fig = go.Figure()
            phys_fig.add_trace(go.Histogram(x=char_1_phys_trials, nbinsx=100, name=char_1.name))
            phys_fig.add_trace(go.Histogram(x=char_2_phys_trials, nbinsx=100, name=char_2.name))
            phys_fig.update_layout(title=char_1.name + ' Has Physical Battle With ' + char_2.name, xaxis_title='Time to Kill [s]', yaxis_title='Number of Times', barmode='overlay', showlegend=True)
            phys_fig.update_traces(opacity=0.5)

            phys_fig.write_image('graphs/battlesim/' + char_1.name.replace(' ', '').lower() + '_pbattle_' + char_2.name.replace(' ', '').lower() + '.png')

            test_count += 1

            print_progress(test_count, total_tests, prefix='MYST >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            myst_trials = [do_battle(char_1, char_2, myst_attack) for i in range(250)]
            char_1_myst_trials = []
            char_2_myst_trials = []

            for trial in myst_trials:
                if char_1.name == trial[1].name:
                    char_1_myst_trials.append(trial[0])
                else:
                    char_2_myst_trials.append(trial[0])

            myst_fig = go.Figure()
            myst_fig.add_trace(go.Histogram(x=char_1_myst_trials, nbinsx=100, name=char_1.name))
            myst_fig.add_trace(go.Histogram(x=char_2_myst_trials, nbinsx=100, name=char_2.name))
            myst_fig.update_layout(title=char_1.name + ' Has Mystical Battle With ' + char_2.name, xaxis_title='Time to Kill [s]', yaxis_title='Number of Times', barmode='overlay', showlegend=True)
            myst_fig.update_traces(opacity=0.5)

            myst_fig.write_image('graphs/battlesim/' + char_1.name.replace(' ', '').lower() + '_mbattle_' + char_2.name.replace(' ', '').lower() + '.png')

            test_count += 1

    print_progress(test_count, total_tests, prefix=' >', suffix='[Done!]')

def do_battle (char_1, char_2, attack):
    char_1.curr_hp = char_1.hp
    char_2.curr_hp = char_2.hp
    char_1.curr_sp = 100
    char_2.curr_sp = 100

    battle_winner = None
    iterations = 0

    while battle_winner == None:
        iterations += 1

        if char_1.curr_sp == 100 and battle_winner == None:
            char_1.curr_hp -= attack.calc_damage(char_1, char_2, integer=True)
            char_1.curr_sp = 0

            if char_2.curr_hp <= 0:
                battle_winner = char_1

        if char_2.curr_sp == 100 and battle_winner == None:
            char_2.curr_hp -= attack.calc_damage(char_2, char_1, integer=True)
            char_2.curr_sp = 0

            if char_1.curr_hp <= 0:
                battle_winner = char_2

        char_1.regain_speed()
        char_2.regain_speed()

    return [iterations, battle_winner]

if __name__ == '__main__':
    sim()
