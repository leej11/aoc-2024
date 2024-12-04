import re


def read_input(input_file):

    with open(input_file) as f:
        txt = f.read()

    return txt



def part1():

    input = read_input('sample.txt')

    matches = re.findall(r'(mul\((\d+),(\d+)\))', input)

    sum = 0
    for match in matches:
        sum += int(match[1]) * int(match[2])

    print(sum)



def part2():

    input = read_input('input.txt')

    rxp = r"(don't\(\)|do\(\)|mul\((\d+),(\d+)\))"
    matches = re.findall(rxp, input)

    sum = 0
    do_active = True
    for match in matches:
        if match[0] == "don't()":
            do_active = False
        elif match[0] == "do()":
            do_active = True
        elif ("mul" in match[0]) and do_active:
            sum += int(match[1]) * int(match[2])
        else:
            continue

    print(sum)


if __name__ == '__main__':

    
    part1()  
    part2()  
