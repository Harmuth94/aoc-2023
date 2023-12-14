import re
import math

def does_finish(wait, time, distance):
    speed = wait
    remaining_time = time - wait
    return distance < speed * remaining_time

def part_one(data):
    races = {}
    time = [int(x) for x in re.sub(' +', ' ', data[0]).split(':')[1].strip().split(' ')]
    distance = [int(x) for x in re.sub(' +', ' ', data[1]).split(':')[1].strip().split(' ')]

    for i in range(len(time)):
        races[i] = {
            'time': time[i],
            'distance': distance[i]
        }

    prod_of_n_ways = 1
    for idx, race in races.items():
        n_ways = 0
        time = race['time']
        distance = race['distance']
        for i in range(time):
            if does_finish(i, time, distance):
                n_ways += 1
        
        prod_of_n_ways *= n_ways
    return prod_of_n_ways


def part_two(data):
    
    time = int(re.sub(' ', '', data[0]).split(':')[1].strip())
    distance = int(re.sub(' ', '', data[1]).split(':')[1].strip())


    root_1 = (-time + (time**2 - 4 * distance) ** 0.5) / -2
    root_2 = (-time - (time**2 - 4 * distance) ** 0.5) / -2
    
    lower_bound = math.ceil(min(root_1, root_2))
    upper_bound = math.floor(max(root_1, root_2))

    return upper_bound - lower_bound + 1


if __name__ == '__main__':
    
    with open('data/input06.txt') as f:
        data = f.read().splitlines()
        

    print(part_one(data))

    print(part_two(data))