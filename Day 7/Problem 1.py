def read_diagram_from_filename(filename):
    diagram = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip()
            diagram.append(list(str))

    return diagram


def get_no_splits_from_start_point_and_diagram(position_of_start_point, diagram):
    no_rows = len(diagram)
    no_cols = len(diagram[0])

    last_row_no = no_rows - 1

    row_no, col_no = position_of_start_point

    for i in range(row_no, no_rows):
        if i == last_row_no or diagram[i][col_no] == '|':
            diagram[i][col_no] = '|'
            return 0
        elif diagram[i][col_no] == '^':
            new_col_no_1 = col_no - 1
            new_col_no_2 = col_no + 1

            ans = 1

            if diagram[i][new_col_no_1] == '.':
                ans += get_no_splits_from_start_point_and_diagram((i, new_col_no_1), diagram)

            if diagram[i][new_col_no_2] == '.':
                ans += get_no_splits_from_start_point_and_diagram((i, new_col_no_2), diagram)

            return ans
        diagram[i][col_no] = '|'
    return None


def get_no_splits_from_diagram(diagram):
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

    return get_no_splits_from_start_point_and_diagram(position_of_start_point, diagram)


def main():
    diagram = read_diagram_from_filename('input/input')
    print(get_no_splits_from_diagram(diagram))


if __name__ == '__main__':
    main()
