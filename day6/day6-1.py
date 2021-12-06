data = [i.strip() for i in open('input2.txt', 'r').read().split(",")]
fish = [data.count(i) for i in "012345678"]
for i in range(80): fish = [*fish[1:7], fish[7]+fish[0], fish[-1], fish[0]]
print(sum(fish))
