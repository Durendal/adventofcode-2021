def main():
    d = [int(i) for i in open('input.txt', 'r').readlines()]
    print(sum([sum(d[i:i+3]) < sum(d[i+1:i+4]) for i in range(0, len(d)-3)]))

if __name__ == '__main__':
    main()
