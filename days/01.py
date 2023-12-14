def first_digit(string):
    for char in string:
        if char.isdigit():
            return char
    return None


def part_one(data):
    return sum([int(first_digit(datum) + first_digit(datum[::-1])) for datum in data])


digit_map = [('one','1'), ('two','2'), ('three','3'), ('four','4'), ('five','5'), ('six','6'), ('seven','7'), ('eight','8'), ('nine','9')]

def first_real_digit(string):
    for idx, char in enumerate(string):
        if char.isdigit():
            return char
        rest_of_string = string[idx:]
        for word, digit in digit_map:
            if rest_of_string.startswith(word):
                return digit
    raise ValueError('No digit found in string')


def last_real_digit(string):
    length = len(string)
    for idx, char in enumerate(string[::-1]):
        if char.isdigit():
            return char
        rest_of_string = string[length-idx-1:]
        for word, digit in digit_map:
            if rest_of_string.startswith(word):
                return digit
    raise ValueError('No digit found in string')



def part_two(data):
    # replace 
    # one, two, three, four, five, six, seven, eight, and nine
    # with 1, 2, 3, 4, 5, 6, 7, 8, and 9
    
    return sum([int(first_real_digit(datum) + last_real_digit(datum)) for datum in data])


if __name__ == '__main__':
    
    with open('data/input01.txt') as f:
        data = f.read().splitlines()

    print(part_one(data))

    print(part_two(data))