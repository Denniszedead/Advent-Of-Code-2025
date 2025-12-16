import math


def get_junction_boxes(filename):
    junction_boxes = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            cord_str = line.strip()
            x, y, z = cord_str.split(',')
            junction_boxes.append((int(x), int(y), int(z)))

    return junction_boxes


def get_euclidean_distance_between_points(point_1, point_2):
    x1, y1, z1 = point_1
    x2, y2, z2 = point_2

    sub_total = math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2) + math.pow(z2 - z1, 2)

    return math.sqrt(sub_total)


def main():
    junction_boxes = get_junction_boxes('input/sample')


if __name__ == '__main__':
    main()

