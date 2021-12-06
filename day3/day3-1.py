d = [i.strip() for i in open('input.txt', 'r').readlines()]
counters = [0 for i in range(12)]
for line in d: 
    for i in range(12):
       if line[i] == "1":
            counters[i] += 1 
gamma = ['1' if counters[i] > 500 else '0' for i in range(len(counters))]
epsilon = ['0' if counters[i] > 500 else '1' for i in range(len(counters))]
print(int(''.join(gamma), 2) * int(''.join(epsilon), 2))
