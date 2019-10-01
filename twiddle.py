'''Create a Node class that holds the parent, board, move made to get to it,
and its current depth.'''
class Node:
    def __init__(self,parentData,boardData,moveData,depthData):
        self.parent = parentData
        self.board = boardData
        self.move = moveData
        self.depth = depthData

    def getParent(self):
        return self.parent

    def getBoard(self):
        return self.board

    def getMove(self):
        return self.move

    def getDepth(self):
        return self.depth

'''This is where the Algorithm actually begins.'''
def search(aString):
    board = aString
    board = switch(board)
    return

def switch(board):

    '''initialize "referal" and "childrenList", these will be used
        when we generate the children and rotate around points'''
    
    referal = {'A':[0,1,3,4],'B':[1,2,4,5],'C':[3,4,6,7],'D':[4,5,7,8]}
    childrenList = ["Ac","Acc","Bc","Bcc","Cc","Ccc","Dc","Dcc"]

    '''Set up our algorithm's queue with the board supplied as the root'''
    root = Node("None",board,"None",0)
    queue = []
    queue.append(root)

    '''Set up counters for nodes and depth as well as set up our while loop'''
    nodeCounter = 0
    CURRENT_DEPTH = 0
    found = False

    while found == False:
        
        '''This will run once every Node that can be checked in each depth has been
            checked. This will place the root back in and thus restart the queue'''
        if queue == []:
            CURRENT_DEPTH += 1
            queue.append(root)

        '''Take the last node out of our FIFO Queue and increment our Node counter'''
        currentNode = queue.pop()
        nodeCounter += 1

        '''Check if the Node we are checking is the goal state, if it is,
            run our "getComplete" function and end the while loop.
            If it is not the goal state, generate its eight children and assign
            their boards by turning each point clockwise or counterclockwise.
            NOTE: This is NOT when we check if a board is the goal state, we are
            only creating them. They will be checked when they become the
            "currentNode"'''
        if currentNode.getBoard() == "123456789":
            getComplete( currentNode, queue, nodeCounter )
            found = True

        else:
            if currentNode.getDepth() < CURRENT_DEPTH:
                for m in childrenList:
                    direction = len(m)

                    if direction == 2:
                        newBoard = clockwise(currentNode.getBoard(),referal[m[0]])
                        newNode = Node(currentNode,newBoard,m,currentNode.getDepth()+1)
                        queue.append(newNode)
                    
                    else:
                        newBoard = counter(currentNode.getBoard(),referal[m[0]])
                        newNode = Node(currentNode,newBoard,m,currentNode.getDepth()+1)
                        queue.append(newNode)

def clockwise(board,coordinate):
    '''Rotate the given board clockwise on the given coordinate'''
    switchList = list(board)
    
    temp = switchList[coordinate[0]]
    switchList[coordinate[0]] = switchList[coordinate[2]]
    switchList[coordinate[2]] = switchList[coordinate[3]]
    switchList[coordinate[3]] = switchList[coordinate[1]]
    switchList[coordinate[1]] = temp
    
    returnlist = ""
    for i in switchList:
        returnlist += i
        
    return returnlist

def counter(board,coordinate):
    '''Rotate the given board counter-clockwise on the given coordinate'''
    switchList = list(board)
    
    temp = switchList[coordinate[0]]
    switchList[coordinate[0]] = switchList[coordinate[1]]
    switchList[coordinate[1]] = switchList[coordinate[3]]
    switchList[coordinate[3]] = switchList[coordinate[2]]
    switchList[coordinate[2]] = temp
    
    returnlist = ""
    for i in switchList:
        returnlist += i
        
    return returnlist

def getComplete( winningNode, queue, counter ):
    '''Output the: path taken to our found solution, nodeCounter, and the
        remaining nodes in the fringe'''
    returnList = []
    while winningNode.getMove() != "None":
        returnList.append(winningNode.getMove())
        winningNode = winningNode.getParent()
    returnList.reverse()
    
    print(returnList)
    print("You can solve this board in",len(returnList),"moves!")
    print("Nodes remaining in fringe:",len(queue))
    print("Nodes expanded during this process:",counter + len(queue))

if __name__ == '__main__':
    '''Change the value of 'USER_INPUT' to a solveable board of 9 characters, look at
    'solveable_boards.txt' for examples to use.'''
    
    USER_INPUT = "675381429"
    
    search( USER_INPUT )
