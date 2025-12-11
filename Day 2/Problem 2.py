import math


def get_ranges_from_file(filename):
    str = ''

    with open(filename) as f:
        str = f.read()

    return str.split(',')

def main():
    ranges = get_ranges_from_file('input/input.txt')
    answer = 0

    for range_str in ranges:
        answer += find_invalid_pattern(range_str)

    print(answer)

def find_invalid_pattern(range_str):
    [start_index, end_index] = breakdown_range(range_str)
    answer = 0

    # Add 1 for the end index as range does not include the end index
    for index in range(start_index, end_index + 1):
        if is_invalid_id(index):
            answer += index

    return answer

def is_invalid_id(number):
    number_string = str(number)
    window_size = 1

    while window_size < len(number_string):
        arr = breakdown_str_by_len(number_string, window_size)

        if if_all_elements_are_the_same(arr):
            return True

        window_size += 1

    return False

def breakdown_str_by_len(given_str, window_len):
    result = []
    no_groups = math.ceil(len(given_str) / window_len)

    for x in range(no_groups):
        start_index = (x * window_len)
        end_index = start_index + window_len

        result.append(given_str[start_index:end_index])

    return result

def if_all_elements_are_the_same(arr):
    if len(arr) <= 1:
        return False

    arr_set = set(arr)

    return len(arr_set) == 1

def breakdown_range(range_str):
    indexes = range_str.split('-')

    return [int(indexes[0]), int(indexes[1])]

if __name__ == "__main__":
    main()
