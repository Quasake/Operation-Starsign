import gspread

from character import Character
from oauth2client.service_account import ServiceAccountCredentials

CHAR_NAME = 0
CHAR_HP = 12
CHAR_MP = 13
CHAR_S = 14
CHAR_D = 15
CHAR_MS = 16
CHAR_F = 17
CHAR_SP = 18
CHAR_E = 19
CHAR_L = 20
CHAR_C = 21

def get_char_stats ():
    print('Accessing spreadsheet...')

    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('dmg_form_google.json', scope)
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

# print(base_attack.calc_damage(characters[0], characters[2]))

# WEBSITE: https://stackoverflow.com/questions/3173320/text-progress-bar-in-the-console
def print_progress_bar (iteration, total, prefix='', suffix='', decimals=1, length=50, fill='█', print_end="\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filled_length = int(length * iteration // total)
    bar = fill * filled_length + '-' * (length - filled_length)

    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end=print_end)

    # Print New Line on Complete
    if iteration == total:
        print()
