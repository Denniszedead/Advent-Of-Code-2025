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

def is_all_vertexes_visited(xs):
    for x in xs:
        if not x:
            return False

    return True

def get_last_point_that_creates_connection(index_1, index_2, junction_boxes):
    (x1, y1, z1) = junction_boxes[index_1]
    (x2, y2, z2) = junction_boxes[index_2]

    print(x1 * x2)

def check_which_point_close_the_junction_box(edge_list, junction_boxes):
    no_vertexes = len(junction_boxes)
    udfs = UFDS(no_vertexes)

    for edge in edge_list:
        index_1, index_2, weight = edge

        if not udfs.is_same_set(index_1, index_2):
            udfs.union_set(index_1, index_2)

            if udfs.is_all_same_set():
                get_last_point_that_creates_connection(index_1, index_2, junction_boxes)
                break


class UFDS:
    def __init__(self, no_vertices):
        self.parent = [x for x in range(no_vertices)]
        self.rank = [0 for _ in range(no_vertices)]

    def find_set(self, vertice_no):
        if self.parent[vertice_no] != vertice_no:
            self.parent[vertice_no] = self.find_set(self.parent[vertice_no])
        return self.parent[vertice_no]

    def is_same_set(self, x, y):
        return self.find_set(x) == self.find_set(y)

    def union_set(self, x, y):
        if not self.is_same_set(x, y):
            x_parent = self.find_set(x)
            y_parent = self.find_set(y)

            if self.rank[x_parent] > self.rank[y_parent]:
                self.parent[y_parent] = x_parent
            else:
                self.parent[x_parent] = y_parent
                if self.rank[x_parent] == self.rank[y_parent]:
                    self.rank[y_parent] += 1

    def is_all_same_set(self):
        for x in range(len(self.parent)):
            self.find_set(x)
        return len(set(self.parent)) == 1


def main():
    junction_boxes = get_junction_boxes('input/input')
    edge_list = get_edge_lists(junction_boxes)
    check_which_point_close_the_junction_box(edge_list, junction_boxes)

if __name__ == "__main__":
    main()
