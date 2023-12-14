def hash_cards(a):
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    hash_map = {
        'A': '14',
        'K': '13',
        'Q': '12',
        'J': '11',
        'T': '10',
    }
    return hash_map.get(a, f'0{a}')


def hand_value(hand: str):

    
    pairs = list()
    for card_val in set(hand):
        pairs.append(hand.count(card_val))

    if 5 in pairs:
        return 7
    if 4 in pairs:
        return 6
    if 3 in pairs:
        if 2 in pairs:
            return 5
        else:
            return 4
    if 2 in pairs:
        if pairs.count(2) == 2:
            return 3
        else:
            return 2
    return 1

def hash_cards_2(a):
    # A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2
    hash_map = {
        'A': '14',
        'K': '13',
        'Q': '12',
        'J': '01',
        'T': '10',
    }
    return hash_map.get(a, f'0{a}')


def hand_value_2(_hand: str):

    
    pairs = list()
    Js = _hand.count('J')
    hand = _hand.replace('J', '')
    for card_val in set(hand):
        pairs.append(hand.count(card_val))

    max_pair = 0 if pairs == [] else max(pairs)
    if max_pair in pairs:
        pairs.remove(max_pair)
    pairs.append(Js + max_pair)

    if 5 in pairs:
        return 7
    if 4 in pairs:
        return 6
    if 3 in pairs:
        if 2 in pairs:
            return 5
        else:
            return 4
    if 2 in pairs:
        if pairs.count(2) == 2:
            return 3
        else:
            return 2
    return 1

def hand_hash(hand: str):
    return str(hand_value(hand)) + ''.join([hash_cards(x) for x in hand])


def hand_hash_2(hand: str):
    return str(hand_value_2(hand)) + ''.join([hash_cards_2(x) for x in hand])


def part_one(data):
    
    hands = [{
                'hand': line.split(' ')[0],
                'bid': int(line.split(' ')[1]),
                'hash': hand_hash(line.split(' ')[0])
            } for line in data]

    hands.sort(key=lambda x: x['hash'])
    print(hands)
    return [x['bid']*(idx + 1) for idx, x in enumerate(hands)]

def part_two(data):
    hands = [{
                'hand': line.split(' ')[0],
                'bid': int(line.split(' ')[1]),
                'hash': hand_hash_2(line.split(' ')[0])
            } for line in data]

    hands.sort(key=lambda x: x['hash'])
    print(hands)
    return [x['bid']*(idx + 1) for idx, x in enumerate(hands)]

if __name__ == '__main__':
        
        with open('data/input07.txt') as f:
            data = f.read().splitlines()
        p1 = part_one(data)
        print(sum(p1))
    
        p2 = part_two(data)
        print(sum(p2))