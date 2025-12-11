def get_ranges_from_file(filename):
    str = ''

    with open(filename) as f:
        str = f.read()

    return str.split(',')

def main():
    ranges = get_ranges_from_file('input/input.txt')
    answer = 0;

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
    half = int(len(number_string) / 2)
    first_half = number_string[:half]
    second_half = number_string[half:]

    return first_half == second_half

def breakdown_range(range_str):
    indexes = range_str.split('-')

    return [int(indexes[0]), int(indexes[1])]

if __name__ == "__main__":
    main()
