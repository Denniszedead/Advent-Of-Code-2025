def get_adjacency_list_from_file(filename):
    return {
        'key': []
    }

def main():
    adjacency_list = get_adjacency_list_from_file('inputs/sample.txt')

    no_rolls_can_remove = 0

    for k, neighbours in adjacency_list.items():
        if len(neighbours) < 4:
            no_rolls_can_remove += 1

    print(no_rolls_can_remove)

if __name__ == '__main__':
    main()

