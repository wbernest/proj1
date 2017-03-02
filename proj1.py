import sys
import time
import math
#import resource
import copy

function = sys.argv[1]
board = sys.argv[2]

class Queue:
    def __init__(self,item):
        self.items = []
        self.items.insert(0,item)
        return

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)
        return

    def dequeue(self):
        return self.items.pop()

    def search(self, item):
        return self.items.count(item) > 0

    def size(self):
        return len(self.items)

class Stack:
    def __init__(self,item):
        self.items = []
        self.items.append(item)
        return

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)
        return 

    def pop(self):
        return self.items.pop()

    def search(self, item):
        return self.items.count(item) > 0

    def size(self):
        return len(self.items)
 
def bfs(data, n):
	start = time.time()
	frontier = Queue((data, ""))
	explored = []
	maxFringeSize = 0
	state = ()
	
	print(data)
	while not frontier.isEmpty():
		if maxFringeSize < frontier.size(): maxFringeSize = frontier.size()
		state = frontier.dequeue()
		explored.append(state[0])
		#print frontier.items
		#print explored
		if state[0] == '012345678': break
		#elif state[0] == 'fail': continue


		#print state	
		#raw_input("key")
		moves = ['Up', 'Down', 'Left', 'Right']	
		for move in moves:
			nextState = getNeighbor(state[0], move)
			if not nextState == 'none' and frontier.search(nextState) == 0 and explored.count(nextState) == 0:
				#print nextState
				#print explored
				#print frontier.items
				frontier.enqueue((nextState, state[1] + "," + move))
		


	#print(explored)
	#print movesMade
	out = {
		'pathToGoal': state[1][1::].split(','),
		'costOfPath': len(state[1][1::].split(',')),
		'nodesExpanded': len(explored)-1,
		'fringeSize': frontier.size(),
		'maxFringeSize': maxFringeSize,
		'searchDepth': len(state[1][1::].split(',')),
		'maxSearchDepth': len(state[1][1::].split(',')),
		'runningTime': 0
    }
	#print out
	end = time.time()
	out['runningTime'] = end - start
	output(out)
	return

def dfs(data, n):
	start = time.time()
	frontier = Stack(data)
	explored = []
	maxFringeSize = 0
	#state = ()
	
	#print(data)
	while not frontier.isEmpty():
		if maxFringeSize < frontier.size(): maxFringeSize = frontier.size()
		state = frontier.pop()
		explored.append(state)
		#print frontier.items
		if state == '012345678':
			break
		
		for neighbor in getNeighbors(state,n):
			if not frontier.search(neighbor) and explored.count(neighbor) == 0:
				frontier.push(neighbor)

	#print(explored)
	#print movesMade
	out = {
		'pathToGoal': state[1][1::].split(','),
		'costOfPath': len(state[1][1::].split(',')),
		'nodesExpanded': len(explored)-1,
		'fringeSize': frontier.size(),
		'maxFringeSize': maxFringeSize,
		'searchDepth': len(state[1][1::].split(',')),
		'maxSearchDepth': len(state[1][1::].split(',')),
		'runningTime': 0
    }
	#print out
	end = time.time()
	out['runningTime'] = end - start
	output(out)
	return

def ast(data, n):
	out = {
		'pathToGoal':"",
		'costOfPath': 0,
		'nodesExpanded': 0,
		'fringeSize': 0,
		'maxFringeSize': 0,
		'searchDepth': 0,
		'maxSearchDepth': 0,
		'runningTime': 0
    }
	start = time.time()
	end = time.time()
	out['runningTime'] = end - start
	output(out)
	return

def ida(data, n):
	out = {
		'pathToGoal':"",
		'costOfPath': 0,
		'nodesExpanded': 0,
		'fringeSize': 0,
		'maxFringeSize': 0,
		'searchDepth': 0,
		'maxSearchDepth': 0,
		'runningTime': 0
    }
	start = time.time()
	end = time.time()
	out['runningTime'] = end - start
	output(out)
	return

def output(data):
    #usage = resource.getrusage(resource.RUSAGE_SELF)
    #outputFile = open("output.txt", "w")
    print("path_to_goal: " + str(data['pathToGoal']) + "\n")
    print("cost_of_path: " + str(data['costOfPath']) + "\n")
    print("nodes_expanded: " + str(data['nodesExpanded']) + "\n")
    print("fringe_size: " + str(data['fringeSize']) + "\n")
    print("max_fringe_size: " + str(data['maxFringeSize']) + "\n")
    print("search_depth: " + str(data['searchDepth']) + "\n")
    print("max_search_depth: " + str(data['maxSearchDepth']) + "\n")
    print("running_time: " + "{:.8f}".format(data['runningTime']) + "\n")
    #outputFile.write("max_ram_usage: " + "{:.8f}".format(usage.ru_maxrss/1028) + "\n")
    return
    
def getNeighbor(state, move):
	numList = state[::-1].split(",")
	zeroX = 0
	zeroY = 0
	
	board = []
	for i in range(0, 3):
		board.append([])
		for j in range(0, 3):
			board[i].append(numList.pop())
			if board[i][j] == "0": 
				zeroX = i
				zeroY = j
	
	if move == 'Up':
		if zeroX > 0:
			board[zeroX][zeroY] = board[zeroX - 1][zeroY]
			board[zeroX - 1][zeroY] = 0
		else:
			return 'none'

	elif move == 'Down':
		if zeroX < 2:
			board[zeroX][zeroY] = board[zeroX + 1][zeroY]
			board[zeroX + 1][zeroY] = 0
		else:
			return 'none'

	elif move == 'Left':
		if zeroY > 0:
			board[zeroX][zeroY] = board[zeroX][zeroY - 1]
			board[zeroX][zeroY - 1] = 0
		else:
			return 'none'
	elif move == 'Right':
		if zeroY < 2:
			board[zeroX][zeroY] = board[zeroX][zeroY + 1]
			board[zeroX][zeroY + 1] = 0
		else:
			return 'none'
	
	returnList = []
	for i in range(0, 3):
		for j in range(0, 3):
			returnList.append(board[i][j])
			
	return ','.join(map(str,returnList))
	
def getNeighbors(state, n):
	moves = ['Up', 'Down', 'Left', 'Right']
	neighbors = []
	stateList = list(state)
	for move in moves:
		numList = copy.copy(stateList)
		zeroIndex = numList.index('0')
		zeroY = 0
	
		if move == 'Up':
			if zeroIndex //  n > 0:
				numList[zeroIndex] = numList[zeroIndex - n]
				numList[zeroIndex - n] = '0'
		elif move == 'Down':
			if zeroIndex //  n < 2:
				numList[zeroIndex] = numList[zeroIndex + n]
				numList[zeroIndex + n] = '0'
		elif move == 'Left':
			if zeroIndex %  n > 0:
				numList[zeroIndex] = numList[zeroIndex - 1]
				numList[zeroIndex - 1] = '0'
		elif move == 'Right':
			if zeroIndex %  n < 2:
				numList[zeroIndex] = numList[zeroIndex + 1]
				numList[zeroIndex + 1] = '0'
		returnList =  ''.join(numList)
	
		if not state == returnList:
			neighbors.insert(0, returnList)
	return neighbors

commaLessState = board.replace(',', '')
n = int(math.sqrt(len(commaLessState)))

if function == "bfs":
 	bfs(commaLessState, n)
elif function == "dfs":
 	dfs(commaLessState, n)
elif function == "ast":
 	ast(commaLessState, n)
elif function == "ida":
	ida(commaLessState, n)
