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


def get_distance_between_points_matrix(junction_boxes):
    no_junction_boxes = len(junction_boxes)
    distance_matrix = [[None for _ in range(no_junction_boxes)] for _ in range(no_junction_boxes)]

    for i in range(no_junction_boxes):
        for j in range(i + 1, no_junction_boxes):
            if i != j:
                point_1 = junction_boxes[i]
                point_2 = junction_boxes[j]
                distance_between_points = get_euclidean_distance_between_points(point_1, point_2)
                distance_matrix[i][j] = distance_between_points
                distance_matrix[j][i] = distance_between_points

    return no_junction_boxes


def get_closest_n_pairs_of_junction_boxes(n, junction_boxes):
   distance_matrix = get_distance_between_points_matrix(junction_boxes)


def main():
    junction_boxes = get_junction_boxes('input/sample')
    get_closest_n_pairs_of_junction_boxes(10, junction_boxes)


if __name__ == '__main__':
    main()

