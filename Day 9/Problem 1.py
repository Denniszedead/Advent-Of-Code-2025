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


def main():
    points = get_points_from_file('input/sample')


if __name__ == "__main__":
    main()

