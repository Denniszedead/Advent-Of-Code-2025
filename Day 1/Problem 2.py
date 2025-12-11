from xxlimited_35 import Null


class DualLinkedListNode():
    def __init__(self, prev, index, next):
        self.prev = prev
        self.index = index
        self.next = next

def read_rotations_from_file(filename):
    arrayStr = '';

    with open(filename) as f:
        for line in f:
            arrayStr += line

    result = arrayStr.splitlines()

    return result

def create_circular_linked_list(no_list):
    first_node = DualLinkedListNode(None, 0, None)
    prev_node = first_node
    new_node = None

    for index in range(1, no_list):
        new_node = DualLinkedListNode(prev_node, index, None)
        prev_node.next = new_node
        prev_node = new_node

    if not (new_node is None):
        new_node.next = first_node
        first_node.prev = new_node

    return first_node

def ref_to_fifty(circular_linked_list):
    ref = circular_linked_list

    while ref.index != 50:
        ref = ref.next

    return ref

def get_password(rotations):
    password = 0
    circular_linked_list = create_circular_linked_list(100)
    ref = ref_to_fifty(circular_linked_list)

    for rotation in rotations:
        [turn_direction, no_steps] =  extract_rotation(rotation)

        for x in range(no_steps):
            if turn_direction == 'L':
                ref = ref.prev
            elif turn_direction == 'R':
                ref = ref.next

            if ref.index == 0:
                password += 1

    print(password)

def extract_rotation(rotation):
    direction = rotation[0]
    no_steps = int(rotation[1:])

    return [direction, no_steps]

def main():
    rotations = read_rotations_from_file('input/input1.txt')
    get_password(rotations)

if __name__ == "__main__":
    main()
