import math
from functools import reduce


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
            point_1 = junction_boxes[i]
            point_2 = junction_boxes[j]
            distance_between_points = get_euclidean_distance_between_points(point_1, point_2)
            distance_matrix[i][j] = distance_between_points
            distance_matrix[j][i] = distance_between_points

    return distance_matrix


def create_adjacency_list_based_on_no_nearest_points(n, distance_matrix):
    distances_between_points_arr = []

    for i in range(len(distance_matrix)):
        for j in range(i + 1, len(distance_matrix[i])):
            distances_between_points_arr.append((i, j, distance_matrix[i][j]))

    distances_between_points_arr.sort(key=lambda x: x[2])
    selected_distances_between_points = distances_between_points_arr[:n]

    adjacency_matrix = {i: [] for i in range(len(distance_matrix))}
    for distance_between_points in selected_distances_between_points:
        point_1, point_2, distance = distance_between_points

        adjacency_matrix[point_1].append(point_2)
        adjacency_matrix[point_2].append(point_1)

    return adjacency_matrix


def find_component_based_on_starting_point(starting_point, adjacency_matrix, visited_arr):
    component = [starting_point]
    queue = [starting_point]
    visited_arr[starting_point] = True

    while queue:
        selected_point = queue.pop()

        for neighbour in adjacency_matrix[selected_point]:
            if not visited_arr[neighbour]:
                visited_arr[neighbour] = True
                component.append(neighbour)
                queue.append(neighbour)

    return component


def find_connected_components(adjacency_matrix):
    visited_arr = [False for _ in range(len(adjacency_matrix))]
    components = []

    for i, visited in enumerate(visited_arr):
        if not visited:
            component = find_component_based_on_starting_point(i, adjacency_matrix, visited_arr)
            components.append(component)

    return components


def find_answer_based_on_components(components):
    components.sort(key=lambda xs: len(xs), reverse=True)
    three_largest_components = components[:3]

    ans = 1

    for component in three_largest_components:
        no_vertex = len(component)
        ans *= no_vertex

    return ans


def get_closest_n_pairs_of_junction_boxes(n, junction_boxes):
   distance_matrix = get_distance_between_points_matrix(junction_boxes)
   adjacency_matrix = create_adjacency_list_based_on_no_nearest_points(n, distance_matrix)
   components = find_connected_components(adjacency_matrix)
   ans = find_answer_based_on_components(components)

   print(ans)


def main():
    junction_boxes = get_junction_boxes('input/sample')
    get_closest_n_pairs_of_junction_boxes(10, junction_boxes)


if __name__ == '__main__':
    main()

