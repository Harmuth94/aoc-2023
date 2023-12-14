import numpy as np


def check_index(data, i, j, seen_numbers, results):
    
    seen_numbers.add((i,j))
    delta_i = range(-1,2)
    delta_j = range(-1,2)
    
    if (i,j) in results:
    

        return results[(i,j)]
    for di in delta_i:
    
        for dj in delta_j:
            if di+i < 0 or dj+j < 0:
                continue
            if di+i >= data.shape[0] or dj+j >= data.shape[1]:
                continue
            if di == dj == 0:
                continue
            if (i+di, j+dj) in seen_numbers:
                continue
            if not (data[i+di, j+dj].isdigit() or data[i+di, j+dj] == '.'):
                return True
            if data[i+di, j+dj].isdigit():
                res = check_index(data, i+di, j+dj, seen_numbers, results)
                results[(i+di, j+dj)] = res
                return res
            
    
    return False


def find_end_of_digits(data, i, j):
    if j >= data.shape[1]:
        return j - 1
    if data[i,j].isdigit():
        return find_end_of_digits(data, i, j + 1)
    else:
        return j - 1


def part_one(data):
    results = []

    symbols = set(np.unique(data))
    symbols.remove('.')
    for i in range(0,10):
        try:
            symbols.remove(str(i))
        except KeyError:
            pass
    seen_idx = set()
    output = 0
    max_i = data.shape[0]
    max_j = data.shape[1]
    for idx, val in np.ndenumerate(data):
        if idx in seen_idx:
            continue
        if val.isdigit():
            digits_end = find_end_of_digits(data, idx[0], idx[1])
            
            number_value = int(''.join(data[idx[0], idx[1]:digits_end+1]))
            
            for j in range(idx[1], digits_end+1):
                seen_idx.add((idx[0],j))
                
            check_matrix = data[
                max(0,idx[0]-1):min(idx[0]+2,max_i), 
                max(0,idx[1]-1):min(digits_end+2,max_j)
            ]

            
            for symbol in symbols:
                if np.any(check_matrix == symbol):

                    output += number_value
                    results.append(number_value)

                    break
            

    return output, results

def part_two(data):
    output = 0
    for idx, val in np.ndenumerate(data):
        if val != '*':
            continue
        
        tmp_data = data.copy()
        tmp_data[[[not x.isdigit() for x in l] for l in tmp_data]] = '.'
        tmp_data[idx] = '*'

        _, gears = part_one(tmp_data)
        if len(gears) > 1:
            
            output += np.prod(gears)
        
    return output

if __name__ == '__main__':
    
    with open('data/input03.txt') as f:
        data = np.array([list(line) for line in f.read().splitlines()])
    

