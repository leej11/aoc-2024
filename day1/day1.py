from collections import Counter

def read_input(input_file):

    with open(input_file) as f:
        input_list = [line.rstrip() for line in f]

    return input_list


def part_1(input_type = 'input'):

    input = read_input(f'day1_{input_type}.txt')

    list1 = []
    list2 = []
    for i in input:
       a, b = i.split()
       list1.append(int(a))
       list2.append(int(b))
    
    diffs = []
    for a, b in zip(sorted(list1), sorted(list2)):
        diff = a - b
        diffs.append(abs(diff))

    print(sum(diffs))


def part_2(input_type = 'input'):

    input = read_input(f'day1_{input_type}.txt')

    list1 = []
    list2 = []
    for i in input:
       a, b = i.split()
       list1.append(int(a))
       list2.append(int(b))

    
    counts_of_list_2 = Counter(list2)

    similarity_scores = []
    for i in list1:
        similarity_score = int(i) * counts_of_list_2[i]
        similarity_scores.append(similarity_score)
        
    print(sum(similarity_scores))



if __name__ == '__main__':

    part_1()
    
    part_2()
