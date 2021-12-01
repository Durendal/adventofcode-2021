def main():
    d = [int(i) for i in open('input.txt', 'r').readlines()]
    print(sum([((d[i]+d[i+1]+d[i+2]) < (d[i+1]+d[i+2]+d[i+3])) for i in range(0, len(d)-3)]))

if __name__ == '__main__':
    main()
