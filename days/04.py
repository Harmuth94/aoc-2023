def part_one(data):
    
    output = 0
    for card in data:
        n_winners = len(card['our'].intersection(card['winning']))
        if n_winners == 0:
            continue
        output += 2 ** (n_winners-1)
    return output


def part_two(data):
    output = 0
    for card in enumerate(data):
        output += recursive_helper(data[card[0]:])

    return output

def recursive_helper(data):

    card = data[0]
    n_winners = len(card['our'].intersection(card['winning']))

    counts = 0
    for n in range(n_winners):
        if n+1 >= len(data):
            break
        counts += recursive_helper(data[n+1:])

    return 1 + counts

if __name__ == '__main__':
    
    with open('data/input04.txt') as f:
        data = [{
            'card': line.split(':')[0].split(' ')[1],
            'winning': set(line.replace('  ',' ').split(':')[1].split('|')[0].strip().split(' ')),
            'our': set(line.replace('  ',' ').split(':')[1].split('|')[1].strip().split(' ')),
        }
        for line in f.read().splitlines()]

    print(part_one(data))

    print(part_two(data))