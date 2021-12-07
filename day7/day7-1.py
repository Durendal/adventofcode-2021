from statistics import mean, median, mode
data = [int(i.strip()) for i in open('input.txt', 'r').read().split(",")]
bases = [round(i) for i in [mean(data), median(data), mode(data)]]
print(int(min([sum([abs(i-base) for i in data]) for base in bases])))

