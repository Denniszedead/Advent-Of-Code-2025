from functools import reduce

import numpy as np

def get_problems_by_filename(filename):
    arr = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip()
            line_arr = split_numbers(str)
            arr.append(line_arr)

    transpose_arr = np.transpose(arr)

    return transpose_arr

def split_numbers(str):
    result = []
    num_str = ''

    for index, x in enumerate(str):
        if len(num_str) == 3:
            result.append(num_str)
            num_str = ''
        else:
            num_str += x

    return result

def solve_problem(problem):
    numbers = problem[:-1]
    operand = problem[-1]

    if operand == '+':
        ans = reduce(lambda x, y: int(x) + int(y), numbers)
    elif operand == '*':
        ans = reduce(lambda x, y: int(x) * int(y), numbers)

    return ans

def main():
    problems = get_problems_by_filename('input/sample.txt')

    grand_total = 0

    for problem in problems:
        grand_total += solve_problem(problem)

    print(grand_total)

if __name__ == '__main__':
    main()
