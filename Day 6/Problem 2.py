from functools import reduce

import numpy as np

def get_problems_by_filename(filename):
    arr = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip('\n')
            arr.append(str)

    return extract_problems_from_array(arr)

def pad_last_row(intended_len, str):
    diff = intended_len - len(str)
    padding = ' ' * diff

    return str + padding

def extract_problems_from_array(arr):
    problems = []
    no_rows = len(arr)
    no_cols = len(arr[0])
    last_row = no_rows - 1

    arr[-1] = pad_last_row(no_cols, arr[-1])

    num_str = ''
    problem = []
    for j in range(no_cols - 1, -1, -1):
        for i in range(no_rows):
            if i == last_row:
                if num_str.strip() == '' and arr[i][j] == ' ':
                    num_str = ''
                    problem = []
                    continue
                num = int(num_str.strip())
                problem.append(num)
                num_str = ''
                if arr[i][j] == '+' or arr[i][j] == '*':
                    problem.append(arr[i][j])
                    problems.append(problem)
                    problem = []
            elif arr[i][j] != '':
                num_str += arr[i][j]

    return problems

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
