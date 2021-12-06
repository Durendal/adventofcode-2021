parse_set = lambda data, index: ([data[i] for i in range(len(data)) if data[i][index] == '0'], [data[i] for i in range(len(data)) if data[i][index] == '1'])

def parse_data(data, index, gam=False):
    zero, one = parse_set(data, index)
    if len(zero) == len(one):
        return one if gam else zero 
    if gam:
        return zero if len(zero) > len(one) else one
    else:
        return zero if len(zero) < len(one) else one

gamma = epsilon = [i.strip() for i in open('input.txt', 'r').readlines()]
for i in range(len(gamma[0])):
    if len(gamma) > 1: gamma = parse_data(gamma, i, True)
    if len(epsilon) > 1: epsilon = parse_data(epsilon, i)

print("Epsilon:", epsilon[0], "Gamma:", gamma[0])
print(int(gamma[0], 2)*int(epsilon[0], 2))

