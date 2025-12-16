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

def get_edge_lists(junction_boxes):
    edge_list = []
    no_junction_boxes = len(junction_boxes)

    for index_1 in range(no_junction_boxes):
        for index_2 in range(index_1 + 1, no_junction_boxes):
            box_1 = junction_boxes[index_1]
            box_2 = junction_boxes[index_2]
            distance = get_euclidean_distance_between_points(box_1, box_2)

            edge_list.append((index_1, index_2, distance))

    edge_list.sort(key=lambda x: x[2])

    return edge_list

def main():
    junction_boxes = get_junction_boxes('input/input')
    edge_lists = get_edge_lists(junction_boxes)

if __name__ == "__main__":
    main()
