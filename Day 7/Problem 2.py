def read_diagram_from_filename(filename):
    diagram = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip()
            diagram.append(list(str))

    return diagram


def get_no_paths_from_start_point_and_diagram(position_of_start_point, diagram):
    no_rows = len(diagram)

    last_row_no = no_rows - 1

    row_no, col_no = position_of_start_point

    for i in range(row_no, no_rows):
        if i == last_row_no:
            return 1
        elif diagram[i][col_no] == '^':
            new_col_no_1 = col_no - 1
            new_col_no_2 = col_no + 1

            ans = 0

            ans += get_no_paths_from_start_point_and_diagram((i, new_col_no_1), diagram)
            ans += get_no_paths_from_start_point_and_diagram((i, new_col_no_2), diagram)

            return ans


def get_no_paths_from_diagram(diagram):
    # (row_no, col_no)
    position_of_start_point = (0, 0)
    is_start_pos_found = False

    for i in range(len(diagram)):
        if is_start_pos_found:
            break

        for j in range(len(diagram[i])):
            if diagram[i][j] == 'S':
                position_of_start_point = (i, j)
                break

    return get_no_paths_from_start_point_and_diagram(position_of_start_point, diagram)


def main():
    diagram = read_diagram_from_filename('input/sample')
    print(get_no_paths_from_diagram(diagram))


if __name__ == '__main__':
    main()
