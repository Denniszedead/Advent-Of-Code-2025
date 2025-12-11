def read_rotations_from_file(filename):
    arrayStr = '';

    with open(filename) as f:
        for line in f:
            arrayStr += line

    result = arrayStr.splitlines()

    return result

def get_password(rotations):
    pointer = 50
    password = 0

    for rotation in rotations:
        direction_and_no_steps = extract_rotation(rotation)
        pointer = turn_pointer(pointer, direction_and_no_steps)

        if pointer == 0:
            password += 1

    print(password)

def extract_rotation(rotation):
    direction = rotation[0]
    no_steps = rotation[1:]

    return {
        'direction': direction,
        'no_steps': no_steps
    }

def turn_pointer(intialPointer, direction_and_no_steps):
    no_steps = int(direction_and_no_steps['no_steps'])

    if direction_and_no_steps['direction'] == 'L':
        pointer_now = intialPointer - no_steps
    elif direction_and_no_steps['direction'] == 'R':
        pointer_now = intialPointer + no_steps

    pointer_now = check_excessive_pointer(pointer_now)


    return pointer_now

def check_excessive_pointer(init_pointer):
    pointer_now = init_pointer
    if pointer_now > 99:
        no_excess = pointer_now - 99
        # Add from -1 as if noExcess = 1 represents one step to the right from 99 which is 0
        pointer_now = -1 + no_excess
    elif pointer_now < 0:
        # 0 minus a negative number will return a positive number
        no_excess = 0 - pointer_now
        # Subtract from 100 as if noExcess = 1 represents one step to the left from 0 which is 99
        pointer_now = 100 - no_excess

    if (pointer_now > 99 or pointer_now < 0):
        pointer_now = check_excessive_pointer(pointer_now)

    return pointer_now

def main():
    rotations = read_rotations_from_file('input/input1.txt')
    get_password(rotations)

if __name__ == "__main__":
    main()
