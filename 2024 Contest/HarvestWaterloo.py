class Position:
    def __init__(self, r, c, char):
        self.row = r
        self.col = c
        self.char = char

def add(queue, curposition):
    queue.append(Position(curposition.row + 1, curposition.col, curposition.char))
    queue.append(Position(curposition.row - 1, curposition.col, curposition.char))
    queue.append(Position(curposition.row, curposition.col + 1, curposition.char))
    queue.append(Position(curposition.row, curposition.col - 1, curposition.char))

R = int(input())
C = int(input())
graph = []

for x in range(R):
    column = input().upper()
    for i in range(len(column)):
        graph.append(Position(x, i, column[i]))

#print(graph)

fr = int(input())
fc = int(input())

Farmer = Position(fr - 1, fc - 1, "h")

queue = [Farmer]
value = 0

visited = set()
#@print("Hi")
while queue:
    curposition = queue.pop(0)
    if curposition.row > R-1 or curposition.col > C-1 or curposition.row < 0 or curposition.col < 0:
        continue
    if (curposition.row, curposition.col) in visited:
        continue
    visited.add((curposition.row, curposition.col))

    for p in graph:
        if curposition.row == p.row and curposition.col == p.col:
            if p.char == "*":
                break
            elif p.char == "L":
                value += 10
            elif p.char == "M":
                value += 5
            elif p.char == "S":
                value += 1
    if p.char != "*":
        add(queue, curposition)

print(value)


