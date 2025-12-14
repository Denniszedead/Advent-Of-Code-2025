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

def find_greatest_col(arr):
    greatest_no_col = 0
    for row in arr:
        if len(row) > greatest_no_col:
            greatest_no_col = len(row)

    return greatest_no_col

def extract_problems_from_array(arr):
    problems = []
    no_rows = len(arr)
    no_cols = find_greatest_col(arr)
    last_row = no_rows - 1

    # Pad rows so that all rows are in the same no of cols
    for i in range(len(arr)):
        arr[i] = pad_last_row(no_cols, arr[i])

    num_str = ''
    problem = []
    for j in range(no_cols - 1, -1, -1):
        for i in range(no_rows):
            if i == last_row:
                #if column is empty
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
            else:
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
    problems = get_problems_by_filename('input/input.txt')

    grand_total = 0

    for problem in problems:
        grand_total += solve_problem(problem)

    print(grand_total)

if __name__ == '__main__':
    main()
