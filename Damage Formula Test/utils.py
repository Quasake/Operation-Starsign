import gspread
import plotly.graph_objects as go

from character import Character
from attack import Attack
from oauth2client.service_account import ServiceAccountCredentials

CHAR_NAME = 0
CHAR_HP = 11
CHAR_MP = 12
CHAR_S = 13
CHAR_D = 14
CHAR_MS = 15
CHAR_F = 16
CHAR_SP = 17
CHAR_E = 18
CHAR_L = 19
CHAR_C = 20

def get_char_stats ():
    print('Accessing spreadsheet...')

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('../dmg_form_google.json', scope)
    client = gspread.authorize(creds)
    sheet = client.open('Stat Planning').sheet1

    sheet_values = sheet.get_all_values()
    char_stats = []

    print('Updating character stats...')

    for row in range(1, len(sheet_values)):
        row_values = sheet_values[row]

        char_name = row_values[CHAR_NAME]

        if char_name == '':
            continue

        char_hp = float(row_values[CHAR_HP])
        char_mp = float(row_values[CHAR_MP])
        char_s = float(row_values[CHAR_S])
        char_d = float(row_values[CHAR_D])
        char_ms = float(row_values[CHAR_MS])
        char_f = float(row_values[CHAR_F])
        char_sp = float(row_values[CHAR_SP])
        char_e = float(row_values[CHAR_E])
        char_l = float(row_values[CHAR_L])
        char_c = float(row_values[CHAR_C])

        char_stats.append(Character(char_name, char_hp, char_mp, char_s, char_d, char_ms, char_f, char_sp, char_e, char_l, char_c))

    return char_stats

def print_progress (iteration, total, prefix='', suffix='', decimals=1):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))

    print(prefix + ' ' + percent + '% [' + str(iteration) + '] ' + suffix)

def create_histogram (data, title, xaxis_title, yaxis_title):
    fig = go.Figure()

    for key in data.keys():
        fig.add_trace(go.Histogram(x=data.get(key), nbinsx=100, name=key))

    fig.update_layout(title=title, xaxis_title=xaxis_title, yaxis_title=yaxis_title, barmode='overlay', showlegend=True)
    fig.update_traces(opacity=0.5 if len(data.keys()) > 1 else 1)

    return fig

def battle_sim (char_1, char_2, attack):
    char_1.curr_hp = char_1.hp
    char_2.curr_hp = char_2.hp
    char_1.curr_sp = 100
    char_2.curr_sp = 100

    battle_winner = None
    iterations = 0

    while battle_winner == None:
        iterations += 1

        if char_1.curr_sp == 100 and battle_winner == None:
            char_2.curr_hp -= attack.calc_damage(char_1, char_2, integer=True)
            char_1.curr_sp = 0

            if char_2.curr_hp <= 0:
                battle_winner = char_1

        if char_2.curr_sp == 100 and battle_winner == None:
            char_1.curr_hp -= attack.calc_damage(char_2, char_1, integer=True)
            char_2.curr_sp = 0

            if char_1.curr_hp <= 0:
                battle_winner = char_2

        char_1.regain_speed()
        char_2.regain_speed()

    return [iterations, battle_winner]
