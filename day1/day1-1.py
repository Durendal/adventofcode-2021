def main():
    d = [int(i) for i in open('input.txt', 'r').readlines()]
    print(sum([d[i] < d[i+1] for i in range(0, len(d)-1)]))

if __name__ == '__main__':
    main()
