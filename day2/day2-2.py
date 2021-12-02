def main():
    d = open('input.txt', 'r').readlines()
    aim = depth = horizontal = 0
    for i in d:
        direction, distance = i.split()
        if direction.strip() == 'forward':
            horizontal += int(distance)
            depth += aim * int(distance)
        else:
            aim = aim - int(distance) if direction.strip() == 'up' else aim + int(distance)
    print(horizontal * depth)

if __name__ == '__main__':
    main()
