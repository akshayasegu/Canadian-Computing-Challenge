class Node:
    def __init__(self,x,y,parentstep):
        self.xcoor = x
        self.ycoor = y
        self.stepnumber = parentstep+1
        self.nextmoves = []
    def encode(self):
        return str(self.xcoor)+","+str(self.ycoor)
    
#Trying to add each possible move from the current position, to the queue
#Queue, currentposition
def add(queue, curposition): 
    queue.append(Node(curposition.xcoor + 2,curposition.ycoor +1,curposition.stepnumber))
    queue.append(Node(curposition.xcoor + 2,curposition.ycoor -1,curposition.stepnumber))
    queue.append(Node(curposition.xcoor - 2,curposition.ycoor +1,curposition.stepnumber))
    queue.append(Node(curposition.xcoor - 2,curposition.ycoor -1,curposition.stepnumber))
    queue.append(Node(curposition.xcoor + 1,curposition.ycoor +2,curposition.stepnumber))
    queue.append(Node(curposition.xcoor + 1,curposition.ycoor -2,curposition.stepnumber))
    queue.append(Node(curposition.xcoor - 1,curposition.ycoor +2,curposition.stepnumber))
    queue.append(Node(curposition.xcoor - 1,curposition.ycoor -2,curposition.stepnumber))

Initial = input()
Final = input()
initposition = Node(int(Initial[0]),int(Initial[2]),-1)
finalposition = Node(int(Final[0]),int(Final[2]),0)
visited = set()
queue = []
queue.append(initposition)
#visited.add(initposition.encode())
while len(queue) != 0:
     #pop the current position
     #Adding each possible move from the current position
     #Check if the current position is the final position
     print(visited)
     print(str(queue))
     curposition = queue.pop(0)
     if curposition.encode() in visited:
         continue
     if curposition.xcoor > 8 or curposition.xcoor < 1 or curposition.ycoor > 8 or curposition.ycoor < 1:
         continue
     add(queue,curposition)
     visited.add(curposition.encode())
     if curposition.xcoor == finalposition.xcoor and curposition.ycoor == finalposition.ycoor:
        print(curposition.stepnumber)
        break

