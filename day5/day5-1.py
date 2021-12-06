print_grid = lambda grid: [print(''.join([str(j) for j in grid[i]])) for i in range(len(grid))]
def parse_coordinates(start, end, grid):
    answer = []
    if start[0] != end[0] and start[1] != end[1]:
        return grid, answer
    for i in range(min([start[1], end[1]]), max([start[1], end[1]])+1):
        for j in range(min([start[0], end[0]]), max([start[0], end[0]])+1):
            if grid[i][j] == '.':
                grid[i][j] = 1
            else:
                grid[i][j] += 1
                answer.append((i, j))
    return grid, answer 

data = [i.strip() for i in open('input.txt', 'r').readlines()]
data = [data[i].split(" -> ") for i in range(len(data))]
data = [[list(map(int, data[i][j].split(","))) for j in range(len(data[i]))] for i in range(len(data))]

grid = [list('.'  * (max([coords[0][0] for coords in [pair for pair in data]])+1)) for i in range(max([coords[0][1] for coords in [pair for pair in data]])+1)]

answers = []
for item in data:
    grid, answer = parse_coordinates(item[0], item[1], grid)
    answers += answer
print('Answer: %d' % len(set(answers)))
#print_grid(grid)
