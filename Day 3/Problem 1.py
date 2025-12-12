def extract_banks_from_file(filename):
    arrayStr = ''

    with open(filename) as f:
        for line in f:
            arrayStr += line

    result = arrayStr.splitlines()

    return result

def find_largest_joultage(bank):
    largest_battery_index = 0

    # -1 as we do not want to loop to the last element
    for i in range(len(bank) - 1):
        if bank[i] > bank[largest_battery_index]:
            largest_battery_index = i

    # the second index starts after the largest index
    second_largest_battery_index = largest_battery_index + 1
    for i in range(second_largest_battery_index, len(bank)):
        if bank[i] > bank[second_largest_battery_index]:
            second_largest_battery_index = i

    digit_str = bank[largest_battery_index] + bank[second_largest_battery_index]
    digit = int(digit_str)

    return digit


def main():
    banks = extract_banks_from_file('input/input.txt')

    total_joultage = 0

    for bank in banks:
        total_joultage += find_largest_joultage(bank)

    print(total_joultage)


if __name__ == "__main__":
    main()