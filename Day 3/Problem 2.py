def extract_banks_from_file(filename):
    arrayStr = ''

    with open(filename) as f:
        for line in f:
            arrayStr += line

    result = arrayStr.splitlines()

    return result

def breakdown_batteries(bank):
    result = []

    for index, num in bank:
        result.append({
            'index': index,
            'num': num
        })

    return result

def find_largest_joultage(bank, digit_len):
    digit_str = ''
    largest_digit_index = 0

    for window_len in range(digit_len - 1, -1, -1):
        end_index = len(bank) - window_len
        for index in range(largest_digit_index, end_index):
            if bank[index] > bank[largest_digit_index]:
                largest_digit_index = index

        digit_str += bank[largest_digit_index]
        largest_digit_index += 1

    return int(digit_str)

def main():
    banks = extract_banks_from_file('input/input.txt')

    total_joultage = 0

    for bank in banks:
        total_joultage += find_largest_joultage(bank, 12)

    print(total_joultage)

if __name__ == "__main__":
    main()
