def check_line(board: list, vertical=True):
    for i in range(len(board)):
        for j in range(len(board[0])):
            row = j if vertical else i
            col = i if vertical else j
            if board[row][col] > 0:
                break
            if j == len(board) -1:
                return True
    return False

def parse_board(board: list, number: int):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if number == board[i][j]:
                # negate numbers to keep track of checked boxes
                board[i][j] *= -1
    return board

def parse_boards(boards: list, numbers: list):
    for number in numbers:
        for i in range(len(boards)):
            if len(boards[i]) == 0:
                break
            boards[i] = parse_board(boards[i], number)
            if check_line(boards[i], False) or check_line(boards[i]):
                total = sum(list(filter(lambda x: x, [sum([x for x in line if x > 0]) for line in boards[i]])))
                return total * number

data = open('input.txt', 'r').read().split("\n\n")
numbers = [int(i) for i in data[0].split(",")]
board_data = data[1:]
boards = [list(filter(lambda x: x, [[int(k) for k in j.split()] for j in board_data[i].split("\n")])) for i in range(len(board_data))]

print(parse_boards(boards, numbers))
