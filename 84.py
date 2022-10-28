from random import shuffle, randint

BOARD_SIZE = 40

MAX_DICE = 4

MAX_TURN = 40000

CC_CARDS = ['G', 'J', *(None for _ in range(14))]
CH_CARDS = ['G', 'J', 'C1', 'E3', 'H2', 'R1', 'NR', 'NR', 'NU', 'B3', *(None for _ in range(6))]

# SPECIAL SQUARES
GO = 0
JAIL = 10
C1 = 11
E3 = 24
H2 = 39
G2J = 30
CC = (None, 2, 17, 33)
CH = (None, 7, 22, 36)
RC = (None, 5, 15, 25, 35)
UC = (None, 12, 28)

def play_one_game():
    shuffle(CC_CARDS)
    shuffle(CH_CARDS)

    positions_freq = [0 for _ in range(BOARD_SIZE)]

    cc_index = ch_index = 0
    position = 0
    consecutive_doubles = 0
    for _ in range(MAX_TURN):
        dice1, dice2 = randint(1, MAX_DICE), randint(1, MAX_DICE)
        position  += (dice1 + dice2)
        if dice1 == dice2:
            consecutive_doubles += 1
        else:
            consecutive_doubles = 0
        if consecutive_doubles >= 3:
            position = JAIL

        if position >= BOARD_SIZE:
            position -= BOARD_SIZE
        
        # G2J
        if position == G2J:
            position = JAIL

        elif position in CC:
            card = CC_CARDS[cc_index]
            cc_index += 1
            if cc_index == 16:
                cc_index = 0
            if card == 'G':position = GO
            elif card == 'J':position = JAIL

        elif position in CH:
            card = CH_CARDS[ch_index]
            ch_index += 1
            if ch_index == 16:
                ch_index = 0
            if card == 'G':position = GO
            elif card == 'J':position = JAIL
            elif card == 'C1':position = C1
            elif card == 'E3':position = E3
            elif card == 'H2':position = H2
            elif card == 'R1':position = RC[1]
            elif card == 'NR':
                if position == CH[1]:position = RC[2]
                elif position == CH[2]:position = RC[3]
                elif position == CH[3]:position = RC[1]
            elif card == 'NU':
                if position == CH[1]:position = UC[1]
                elif position == CH[2]:position = UC[2]
                elif position == CH[3]:position = UC[1]
            elif card == 'B3':
                position -= 3
                if position < 0:
                    position += BOARD_SIZE

        positions_freq[position] += 1

    return positions_freq

all_positions = [0 for _ in range(BOARD_SIZE)]

for _ in range(1000):
    positions = play_one_game()

    all_positions = [all_positions[i] + positions[i] for i in range(BOARD_SIZE)]

TOTAL = sum(all_positions)

sorted_positions = sorted(((round(100 * all_positions[i] / TOTAL, 2), i) for i in range(BOARD_SIZE)), key=lambda tup:-tup[0])

print(f'{sorted_positions[0][1]:02}{sorted_positions[1][1]:02}{sorted_positions[2][1]:02}')
