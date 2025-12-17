def get_points_from_file(filename):
    points = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            point_str = line.strip()
            x_str, y_str = point_str.split(',')
            x = int(x_str)
            y = int(y_str)
            points.append((x, y))

    return points


def get_area_based_on_points(point_1, point_2):
    x1, y1 = point_1
    x2, y2 = point_2

    # +1 to both the width and height as when calculating the width and height, need to include the row and col
    # of the starting point
    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1

    return width * height


def get_largest_area(points):
    largest_area = 0

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            point_1 = points[i]
            point_2 = points[j]

            area = get_area_based_on_points(point_1, point_2)

            if area > largest_area:
                largest_area = area

    print(largest_area)


def main():
    points = get_points_from_file('input/input')
    get_largest_area(points)


if __name__ == "__main__":
    main()

