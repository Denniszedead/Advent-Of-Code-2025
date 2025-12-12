def extract_banks_from_file(filename):
    banks = []

    with open(filename, mode='r', encoding="utf-8") as file:
        for line in file:
            banks.append(line)

    return banks

def find_largest_joultage(bank):
    return 0

def main():
    banks = extract_banks_from_file('input/sample.txt')

    total_joultage = 0

    for bank in banks:
        total_joultage += find_largest_joultage(bank)

    print(total_joultage)


if __name__ == "__main__":
    main()