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
	frontier = Queue(data)
	explored = set()
	frontierSet = set()
	frontierSet.add(data)
	parents = {}
	parents[data] = ('None', 'None')
	maxFringeSize = 0
	state = ''
	lastFringeValue = ''
	while not frontier.isEmpty():
		if maxFringeSize < frontier.size(): maxFringeSize = frontier.size()
		state = frontier.dequeue()
		frontierSet.remove(state)
		explored.add(state)
		if state == '012345678':
			break
		
		for neighbor in reversed(getNeighbors(state,n)):
			if neighbor[0] not in frontierSet.union(explored):
				frontier.enqueue(neighbor[0])
				frontierSet.add(neighbor[0])
				parents[neighbor[0]] = (state, neighbor[1])
				lastFringeValue = neighbor[0]

	path = [state]
	words = [parents[state][1]]
	while not path[len(path) - 1] == data:
		path.append(parents[path[len(path) - 1]][0])
		words.append(parents[path[len(path) - 1]][1])

	path = [lastFringeValue]
	while not path[len(path) - 1] == data:
		path.append(parents[path[len(path) - 1]][0])
	words.remove('None')
	words.reverse()
	out = {
		'pathToGoal': words,
		'costOfPath': len(words),
		'nodesExpanded': len(explored)- 1,
		'fringeSize': frontier.size(),
		'maxFringeSize': maxFringeSize,
		'searchDepth': len(words),
		'maxSearchDepth': len(path) - 1,
		'runningTime': 0
    }
	end = time.time()
	out['runningTime'] = end - start
	output(out)
	return

def dfs(data, n):
	start = time.time()
	frontier = Stack(data)
	explored = set()
	frontierSet = set()
	frontierSet.add(data)
	parents = {}
	parents[data] = ('None', 'None')
	maxFringeSize = 0
	state = ''
	lastFringeValue = ''
	while not frontier.isEmpty():
		if maxFringeSize < frontier.size(): maxFringeSize = frontier.size()
		state = frontier.pop()
		frontierSet.remove(state)
		explored.add(state)
		if state == '012345678':
			break
		
		for neighbor in getNeighbors(state,n):
			if neighbor[0] not in frontierSet.union(explored):
				frontier.push(neighbor[0])
				frontierSet.add(neighbor[0])
				parents[neighbor[0]] = (state, neighbor[1])
				lastFringeValue = neighbor[0]

	path = [state]
	words = [parents[state][1]]
	while not path[len(path) - 1] == data:
		path.append(parents[path[len(path) - 1]][0])
		words.append(parents[path[len(path) - 1]][1])

	path = [lastFringeValue]
	while not path[len(path) - 1] == data:
		path.append(parents[path[len(path) - 1]][0])
	words.remove('None')
	words.reverse()
	out = {
		'pathToGoal': words,
		'costOfPath': len(words),
		'nodesExpanded': len(explored)- 1,
		'fringeSize': frontier.size(),
		'maxFringeSize': maxFringeSize,
		'searchDepth': len(words),
		'maxSearchDepth': len(path) - 1,
		'runningTime': 0
    }
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
			neighbors.insert(0, (returnList, move))
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
