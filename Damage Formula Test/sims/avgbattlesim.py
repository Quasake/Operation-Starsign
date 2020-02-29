import sys
sys.path.insert(1, '../')

import math
import plotly.graph_objects as go

from character import Character
from attack import Attack
from utils import *

def sim ():
    characters = get_char_stats()
    avg_char = get_average_character(characters)

    phys_average = []
    myst_average = []

    test_count = 0
    total_tests = len(characters) * 2

    print('Running tests...[Total tests : ' + str(total_tests) + ']')

    for char in characters:
        print_progress(test_count, total_tests, prefix='PHYS >', suffix='[' + char.name + ' >x< ' + avg_char.name + ']')

        phys_trials = [battle_sim(char, avg_char, PHYS_ATTACK) for i in range(2500)]

        phys_data = {char.name: [], avg_char.name: []}
        for trial in phys_trials:
            phys_data[char.name if char.name == trial[1].name else avg_char.name].append(trial[0])

        phys_average.extend(phys_data[char.name])
        phys_average.extend(phys_data[avg_char.name])

        phys_fig = create_histogram(phys_data, char.name + ' Has Physical Battle With ' + avg_char.name, 'Time to Kill [s]')
        phys_fig.write_image('../graphs/avgbattlesim/' + char.name.replace(' ', '').lower() + '_pbattle_' + avg_char.name.replace(' ', '').lower() + '.png')

        test_count += 1

        print_progress(test_count, total_tests, prefix='MYST >', suffix='[' + char.name + ' >x< ' + avg_char.name + ']')

        myst_trials = [battle_sim(char, avg_char, MYST_ATTACK) for i in range(2500)]

        myst_data = {char.name: [], avg_char.name: []}
        for trial in myst_trials:
            myst_data[char.name if char.name == trial[1].name else avg_char.name].append(trial[0])

        myst_average.extend(myst_data[char.name])
        myst_average.extend(myst_data[avg_char.name])

        myst_fig = create_histogram(myst_data, char.name + ' Has Mystical Battle With ' + avg_char.name, 'Time to Kill [s]')
        myst_fig.write_image('../graphs/avgbattlesim/' + char.name.replace(' ', '').lower() + '_mbattle_' + avg_char.name.replace(' ', '').lower() + '.png')

        test_count += 1

    print_progress(test_count, total_tests, prefix=' >', suffix='[Done!]')

    print('Average Physical Battle Time : ' + str(average(phys_average)))
    print('Average Mystical Battle Time : ' + str(average(myst_average)))

def get_average_character (characters):
    hp_arr = []
    mp_arr = []
    s_arr = []
    d_arr = []
    ms_arr = []
    f_arr = []
    sp_arr = []
    e_arr = []
    l_arr = []
    c_arr = []

    for character in characters:
        hp_arr.append(character.hp)
        mp_arr.append(character.mp)
        s_arr.append(character.s)
        d_arr.append(character.d)
        ms_arr.append(character.ms)
        f_arr.append(character.f)
        sp_arr.append(character.sp)
        e_arr.append(character.e)
        l_arr.append(character.l)
        c_arr.append(character.c)

    hp_avg = average(hp_arr)
    mp_avg = average(mp_arr)
    s_avg = average(s_arr)
    d_avg = average(d_arr)
    ms_avg = average(ms_arr)
    f_avg = average(f_arr)
    sp_avg = average(sp_arr)
    e_avg = average(e_arr)
    l_avg = average(l_arr)
    c_avg = average(c_arr)

    return Character('Hugh G. Aynuss', hp_avg, mp_avg, s_avg, d_avg, ms_avg, f_avg, sp_avg, e_avg, l_avg, c_avg)

if __name__ == '__main__':
    sim()
