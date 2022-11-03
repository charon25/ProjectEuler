SORT_ORDER = {str(k): k for k in range(2, 10)}
SORT_ORDER.update({'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14})

def get_hand_value(hand: list[tuple[str, str]]):
    hand.sort(key=lambda card: (SORT_ORDER[card[0]], card[1]))
    values = tuple(SORT_ORDER[card[0]] for card in hand)
    suits = tuple(card[1] for card in hand)

    counter = {}
    for value in values:
        counter[value] = counter.get(value, 0) + 1
    counter = tuple((value, count) for value, count in sorted(counter.items(), key=lambda key_value: key_value[1], reverse=True))

    suits_set = set(suits)

    # Royal Flush
    if values == (10, 11, 12, 13, 14) and len(suits_set) == 1:
        return (10, 0, values[::-1])
    
    # Straight Flush
    if all(v2 == v1 + 1 for v1, v2 in zip(values, values[1:])) and len(suits_set) == 1:
        return (9, values[-1], values[::-1])

    # Four of a Kind
    if counter[0][1] == 4:
        return (8, counter[0][0], values[::-1])

    #Full House
    if counter[0][1] == 3 and counter[1][1] == 2:
        return (7, counter[0][0], values[::-1])

    # Flush
    if len(suits_set) == 1:
        return (6, values[-1], values[::-1])

    # Straight
    if all(v2 == v1 + 1 for v1, v2 in zip(values, values[1:])):
        return (5, values[-1], values[::-1])

    # Three of a Kind
    if counter[0][1] == 3:
        return (4, counter[0][0], values[::-1])

    # Two Pairs
    if counter[0][1] == 2 and counter[1][1] == 2:
        return (3, max(counter[0][0], counter[1][0]), values[::-1])

    # One Pair
    if counter[0][1] == 2:
        return (2, counter[0][0], values[::-1])
    
    return (1, values[-1], values[::-1])


with open('54.txt', 'r') as fi:
    games = fi.read().splitlines()

count = 0

for game in games:
    game = game.split(' ')
    p1_hand = game[:5]
    p2_hand = game[5:]

    if get_hand_value(p1_hand) > get_hand_value(p2_hand):
        count += 1

print(count)
