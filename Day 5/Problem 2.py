def get_ranges_from_file(filename):
    range_list = []
    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip()
            if str == '':
                break
            range_list.append(str)

    acceptable_ranges = get_ranges(range_list)

    return acceptable_ranges

def get_ranges(range_list):
    acceptable_range = []

    for range_str in range_list:
        start_index_str, end_index_str = range_str.split('-')
        start_index = int(start_index_str)
        end_index = int(end_index_str)

        acceptable_range.append((start_index, end_index))

    acceptable_range.sort(key=lambda x: x[0])

    return acceptable_range

def get_new_range(last_range, selected_range):
    if selected_range[0] <= last_range[0]:
        new_start = selected_range[0]
    else:
        new_start = last_range[0]

    if selected_range[1] >= last_range[1]:
        new_end = selected_range[1]
    else:
        new_end = last_range[1]

    return new_start, new_end

def clear_overlapping_ranges(ranges):
    new_ranges = [ranges[0]]
    is_changed = False
    for index in range(1, len(ranges)):
        selected_range = ranges[index]
        last_range = new_ranges[-1]

        if last_range[1] < selected_range[0]:
            new_ranges.append(selected_range)
        else:
            new_ranges[-1] = get_new_range(last_range, selected_range)
            is_changed = True

    new_ranges.sort(key=lambda x: x[0])

    if is_changed:
        return clear_overlapping_ranges(new_ranges)
    else:
        return new_ranges

def main():
    acceptable_ranges = get_ranges_from_file('input/input.txt')
    acceptable_ranges = clear_overlapping_ranges(acceptable_ranges)

    no_acceptable_ingredients = 0

    for range_tup in acceptable_ranges:
        no_ids = (range_tup[1] - range_tup[0]) + 1
        no_acceptable_ingredients += no_ids

    print(no_acceptable_ingredients)

if __name__ == "__main__":
    main()