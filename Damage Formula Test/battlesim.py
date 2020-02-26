import math
import time
import sys
import plotly.graph_objects as go
import numpy as np

from itertools import combinations_with_replacement
from threading import Thread
from character import Character
from attack import Attack
from utils import *

BATTLE_START_TIME = 0
BATTLE_WINNER = None

def sim ():
    characters = get_char_stats()
    combins = list(combinations_with_replacement(characters, 2))

    phys_attack = Attack('Physical Attack', 10, 1, 1)
    myst_attack = Attack('Mystical Attack', 10, 1, 0)

    test_count = 0
    total_tests = math.factorial(len(characters)) / (math.factorial(len(characters) - 2) * math.factorial(2))

    print('Running tests...[Total tests : ' + str(total_tests) + ']')

    for comb in combins:
        char_1 = comb[0]
        char_2 = comb[1]

        if (char_1.name == 'Barthon Vandera' and char_2.name == 'Roy Andrews') or (char_2.name == 'Barthon Vandera' and char_1.name == 'Roy Andrews'):
            print_progress(test_count, total_tests, prefix='SKIP >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            test_count += 1
            continue

        if char_1.name != char_2.name:
            print_progress(test_count, total_tests, prefix='PHYS >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            phys_trials = [do_battle(char_1, char_2, phys_attack) for i in range(75)]
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

            print_progress(test_count, total_tests, prefix='MYST >', suffix='[' + char_1.name + ' >x< ' + char_2.name + ']')

            myst_trials = [do_battle(char_1, char_2, myst_attack) for i in range(75)]
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
    global BATTLE_START_TIME
    global BATTLE_WINNER

    char_1.curr_hp = char_1.hp
    char_2.curr_hp = char_2.hp
    char_1.curr_sp = 100
    char_2.curr_sp = 100

    char_1_thread = Thread(target=regain_speed_thread, args=(char_1,))
    char_2_thread = Thread(target=regain_speed_thread, args=(char_2,))

    BATTLE_WINNER = None
    BATTLE_START_TIME = time.time()

    char_1_thread.start()
    char_2_thread.start()

    while BATTLE_WINNER == None:
        if char_1.curr_sp == 100 and BATTLE_WINNER == None:
            char_1.curr_hp -= attack.calc_damage(char_1, char_2, integer=True)
            char_1.curr_sp = 0

            if char_2.curr_hp <= 0:
                BATTLE_WINNER = char_1

        if char_2.curr_sp == 100 and BATTLE_WINNER == None:
            char_2.curr_hp -= attack.calc_damage(char_2, char_1, integer=True)
            char_2.curr_sp = 0

            if char_1.curr_hp <= 0:
                BATTLE_WINNER = char_2

    char_1_thread.join()
    char_2_thread.join()

    total_time = (time.time() - BATTLE_START_TIME) * 60

    return [total_time, BATTLE_WINNER]

def regain_speed_thread (char):
    global BATTLE_START_TIME
    global BATTLE_WINNER

    delta = 0
    last_update_time = BATTLE_START_TIME

    while BATTLE_WINNER == None:
        delta += (time.time() - last_update_time) / 60

        if delta >= 1:
            char.regain_speed()

            delta -= 1

if __name__ == '__main__':
    sim()
