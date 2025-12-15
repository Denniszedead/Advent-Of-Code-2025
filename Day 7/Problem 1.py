def read_diagram_from_filename(filename):
    diagram = []

    with open(filename, mode='r', encoding='utf-8') as file:
        for line in file:
            str = line.strip()
            diagram.append(str)

    return diagram

def main():
    diagram = read_diagram_from_filename('input/sample')

if __name__ == '__main__':
    main()
