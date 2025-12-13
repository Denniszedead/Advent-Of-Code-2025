def get_range_of_fresh_ids_and_list_of_ingredients(filename):
    ingredient_list = []
    range_list = []
    with open(filename, mode='r', encoding='utf-8') as file:
        is_ingredient_list = False
        for line in file:
            str = line.strip()
            if str == '':
                is_ingredient_list = True
                continue

            if is_ingredient_list:
                ingredient_list.append(int(str))
            else:
                range_list.append(str)

    acceptable_ranges = get_ranges(range_list)

    return acceptable_ranges, ingredient_list

def get_ranges(range_list):
    acceptable_range = []

    for range_str in range_list:
        start_index_str, end_index_str = range_str.split('-')
        start_index = int(start_index_str)
        end_index = int(end_index_str)

        acceptable_range.append((start_index, end_index))

    acceptable_range.sort(key=lambda x: x[0])

    return acceptable_range

def is_num_in_range(num, ranges):
    for range_str in ranges:
        start_index, end_index = range_str
        if start_index <= num <= end_index:
            return True

    return False

def main():
    acceptable_ranges, ingredient_list = get_range_of_fresh_ids_and_list_of_ingredients('input/input.txt')

    no_acceptable_ingredients = 0

    for ingredient in ingredient_list:
        if is_num_in_range(ingredient, acceptable_ranges):
            no_acceptable_ingredients += 1


    print(no_acceptable_ingredients)

if __name__ == "__main__":
    main()
