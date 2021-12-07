from statistics import mean, median, mode
data = [int(i.strip()) for i in open('input.txt', 'r').read().split(",")]
bases = [int(i) for i in [mean(data), median(data), mode(data)]]
print(min([sum([abs(base-number)*(abs(base-number)+1)/2 for number in data]) for base in bases]))

