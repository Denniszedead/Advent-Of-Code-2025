def get_adjacency_list(matrix):
    adjacency_matrix = {}

    for row_no, row in enumerate(matrix):
        for col_no, col in enumerate(row):
            if col == '@':
                node = (row_no, col_no)
                neighbours = get_neighbours(node, matrix)
                row_col_key = ','.join([str(row_no), str(col_no)])
                adjacency_matrix[row_col_key] = neighbours

    return adjacency_matrix

def get_neighbours(node, matrix):
    cur_row_no, cur_col_no = node
    max_row = len(matrix)
    max_col = len(matrix[0])
    neighbours = []

    # + 2 to the cur_row_no as end case as cur_row_no + 1 will be read as the last arr since range will not read cur_row_no + 2
    for selected_row in range(cur_row_no - 1, cur_row_no + 2):
        # + 2 to the cur_col_no as end case as cur_col_no + 1 will be read as the last arr since range will not read cur_col_no + 2
        for selected_col in range(cur_col_no - 1, cur_col_no + 2):
            if selected_row < 0 or selected_row >= max_row:
                continue
            if selected_col < 0 or selected_col >= max_col:
                continue
            if not (selected_row == cur_row_no and selected_col == cur_col_no):
                if matrix[selected_row][selected_col] == '@':
                    neighbours.append((selected_row, selected_col))

    return neighbours

def extract_matrix_from_file(filename):
    arrayStr = ''

    with open(filename) as f:
        for line in f:
            arrayStr += line

    result = arrayStr.splitlines()

    return result

def remove_node_from_adjacency_list(node, adjacency_list):
    neighbours = adjacency_list[node]
    deleted_row_no, deleted_col_no = node.split(',')

    for neighbour in neighbours:
        row_no, col_no = neighbour
        key_str = ','.join([str(row_no), str(col_no)])
        adjacency_list[key_str] = remove_item_from_list((int(deleted_row_no), int(deleted_col_no)), adjacency_list[key_str])

    adjacency_list.pop(node)

    return adjacency_list

def remove_item_from_list(item, xs):
    index = xs.index(item)
    xs.pop(index)

    return xs

def main():
    roll_matrix = extract_matrix_from_file('inputs/input.txt')
    adjacency_list = get_adjacency_list(roll_matrix)

    no_rolls_removed = 0

    while True:
        # Make a copy of the adjacency_list as iterating over existing adjacency_list will return an error
        list_of_nodes = adjacency_list.copy().items()
        is_changed = False
        for k, neighbours in list_of_nodes:
            if len(neighbours) < 4:
                adjacency_list = remove_node_from_adjacency_list(k, adjacency_list)
                is_changed = True
                no_rolls_removed += 1
        if not is_changed:
            break

    print(no_rolls_removed)

if __name__ == '__main__':
    main()

