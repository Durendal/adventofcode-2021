def main():
    d = open('input.txt', 'r').readlines()
    x = y = 0
    for i in d:
        direction, distance = i.split()
        if direction.strip() == 'forward':
            x += int(distance)
        else:
            y = y + int(distance) if direction.strip() == 'down' else y - int(distance)
    print(x*y)

if __name__ == '__main__':
    main()
