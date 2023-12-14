def parse_data(data):
    instructions = data[0]
    lr_map = {}
    for mapping in data[2:]:
        _from = mapping.split(' =')[0] 
        left = mapping[7:10]
        right = mapping[12:15]
        lr_map[_from] = {'L':left, 'R':right}

    return instructions, lr_map

def part_one(data):
    instructions, lr_map = parse_data(data)

    output = 0
    location = 'AAA'
    while True:
        lr = instructions[output % len(instructions)]
        location = lr_map[location][lr]
        output += 1
        if location == 'ZZZ':
            return output
    
def part_two(data):
    instructions, lr_map = parse_data(data)

    locations = [x for x in lr_map.keys() if x[2] == 'A']
    cycles = []
    for location in locations:
        
        output = 0
        while True:
            start = location
            zs = []
            for idx, lr in enumerate(instructions):
                location = lr_map[location][lr]

                if location[2] == 'Z':
                    zs.append(idx)

            if location == start: # detected loop
                break
            output += 1   

        cycles.append({'start': output, 'zs': zs})

if __name__ == '__main__':
        
    with open('data/input08.txt') as f:
        data = f.read().splitlines()
    
    #print(part_one(data))
    print(part_two(data))
