def extract_banks_from_file(filename):
    return []

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