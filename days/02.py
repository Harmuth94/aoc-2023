import re
import numpy as np

def part_one(data):
    output = 0
    max_colors = np.array([12, 13, 14])
    for game in data:
        game_number = int(re.search(r'Game (\d+)', game).group(1))
        unparsed_games = game.split(': ')[-1].split('; ')

        parsed_games = np.array([parse_game(game) for game in unparsed_games])

        if np.all(parsed_games <= max_colors):
            output += game_number

    return output

def part_two(data):
    
    output = 0
    for game in data:
        
        unparsed_games = game.split(': ')[-1].split('; ')

        parsed_games = np.array([parse_game(game) for game in unparsed_games])

        output += np.prod(parsed_games.max(axis=0))

    return output


def color_or_0(string, color):
    m  = re.search(f'(\d+) {color}', string)
    if m:
        return int(m.group(1))
    else:
        return 0

def parse_game(game):
    n_green = color_or_0(game, 'green')
    n_blue = color_or_0(game, 'blue')
    n_red = color_or_0(game, 'red')

    return np.array([n_red, n_green, n_blue])


if __name__ == '__main__':
    
    with open('data/input02.txt') as f:
        data = f.read().splitlines()

    

    print(part_one(data))

    print(part_two(data))
    