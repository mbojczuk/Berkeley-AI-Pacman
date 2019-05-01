# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

#node class
class Node:
    def __init__(self, position, direction, cost):
        self.position = position
        self.direction = direction
        self.cost = cost
        self.parent = None

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]
    
def depthFirstSearch(problem):
    """Search the deepest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    #initialisers
    visited = []                                    #list of visited nodes
    stack = util.Stack()                            #Stack for DFS
    finalPath = []                                  #list of final directions
    
    #newNode is the initial node
    newNode = Node(problem.getStartState(),None, None)
    
    #push first node to the stack
    stack.push(newNode)
    
    print(newNode.position)
    
    #While stack is not empty
    while(not stack.isEmpty()):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #gets node by popping back end of the stack(follows last in first out)
        currentNode = stack.pop()
        #get the current position we are at
        currentPosition = currentNode.position
        print("CurPos after stack pop", currentPosition)
        #check if node exists in visited else put it in the list 
        if(currentPosition in visited):
            print("have already visited")
            continue
        else:
            print("appending to list: ", currentPosition)
            visited.append(currentPosition)
    
        #check if we have reached the food
        if(problem.isGoalState(currentPosition) == True):
            print("reached goal")
            break
            
        #Loop to look at the children of the current node position
        for child in problem.getSuccessors(currentPosition):
            if(child[0] not in visited):
                print("child of pos: ", child[0])
                print("child direction: ", child[1])
                print("child cost: ", child[2])
                #create a new node with constructor
                newNode = Node(child[0], child[1], child[2])
                #give the newNode the parent node
                newNode.parent = currentNode
                print("parent pos", newNode.parent.position)
                #push newNode to stack
                stack.push(newNode)
    
    while(currentNode.direction != None):
        #insert at the front of the list 
        finalPath.insert(0, currentNode.direction)
        #make currentNode = to the previous nodes parent and work up the list
        currentNode = currentNode.parent

    return finalPath
    
    

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    
    #initialisers
    visited = []                                    #list of visited nodes
    queue = util.Queue()                            #Queue for BFS
    finalPath = []                                  #list of final directions
    
    #newNode is the initial node
    newNode = Node(problem.getStartState(),None, None)
    
    #push first node to the stack
    queue.push(newNode)
    
    print(newNode.position)
    
    #While queue is not empty
    while(not queue.isEmpty()):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #gets node by popping front end of the queue(follows first in first out)
        currentNode = queue.pop()
        #get the current position we are at
        currentPosition = currentNode.position
        print("CurPos after stack pop", currentPosition)
        #check if node exists in visited else put it in the list 
        if(currentPosition in visited):
            print("have already visited")
            continue
        else:
            print("appending to list: ", currentPosition)
            visited.append(currentPosition)
    
        #check if we have reached the food
        if(problem.isGoalState(currentPosition) == True):
            print("reached goal")
            break
            
        #Loop to look at the children of the current node position
        for child in problem.getSuccessors(currentPosition):
            if(child[0] not in visited):
                print("child of pos: ", child[0])
                print("child direction: ", child[1])
                print("child cost: ", child[2])
                #create a new node with constructor
                newNode = Node(child[0], child[1], child[2])
                #give the newNode the parent node
                newNode.parent = currentNode
                print("parent pos", newNode.parent.position)
                #push newNode to queue
                queue.push(newNode)
    
    while(currentNode.direction != None):
        #insert at the front of the list 
        finalPath.insert(0, currentNode.direction)
        #make currentNode = to the previous nodes parent and work up the list
        currentNode = currentNode.parent

    return finalPath

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #initialisers
    visited = []                                    #list of visited nodes
    priorityQueue = util.PriorityQueue()            #PriorityQueue for UCS
    finalPath = []                                  #list of final directions
    
    #newNode is the initial node
    newNode = Node(problem.getStartState(),None, None)
    
    #push first node to the stack
    priorityQueue.push(newNode, newNode.cost)
    
    print(newNode.position)
    
    #While queue is not empty
    while(not priorityQueue.isEmpty()):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #gets node by popping back end of the queue(follows first in first out)
        currentNode = priorityQueue.pop()
        #get the current position we are at
        currentPosition = currentNode.position
        print("CurPos after stack pop", currentPosition)
        #check if node exists in visited else put it in the list 
        if(currentPosition in visited):
            print("have already visited")
            continue
        else:
            print("appending to list: ", currentPosition)
            visited.append(currentPosition)
    
        #check if we have reached the food
        if(problem.isGoalState(currentPosition) == True):
            print("reached goal")
            break
            
        #Loop to look at the children of the current node position
        for child in problem.getSuccessors(currentPosition):
            if(child[0] not in visited):
                print("child of pos: ", child[0])
                print("child direction: ", child[1])
                print("child cost: ", child[2])
                #create a new node with constructor
                newNode = Node(child[0], child[1], child[2])
                #give the newNode the parent node
                newNode.parent = currentNode
                print("parent pos", newNode.parent.position)
                #push newNode to queue
                priorityQueue.push(newNode, newNode.cost)
    
    while(currentNode.direction != None):
        #insert at the front of the list 
        finalPath.insert(0, currentNode.direction)
        #make currentNode = to the previous nodes parent and work up the list
        currentNode = currentNode.parent

    return finalPath

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    #initialisers
    visited = []                                    #list of visited nodes
    priorityQueue = util.PriorityQueue()            #PriorityQueue for A*
    finalPath = []                                  #list of final directions
    
    #newNode is the initial node
    newNode = Node(problem.getStartState(),None, None)
    
    #push first node to the stack
    priorityQueue.push(newNode, newNode.cost)
    
    print(newNode.position)
    
    #While queue is not empty
    while(not priorityQueue.isEmpty()):
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        #gets node by popping back end of the queue(follows first in first out)
        currentNode = priorityQueue.pop()
        #get the current position we are at
        currentPosition = currentNode.position
        print("CurPos after stack pop", currentPosition)
        #check if node exists in visited else put it in the list 
        if(currentPosition in visited):
            print("have already visited")
            continue
        else:
            print("appending to list: ", currentPosition)
            visited.append(currentPosition)
    
        #check if we have reached the food
        if(problem.isGoalState(currentPosition) == True):
            print("reached goal")
            break
            
        #Loop to look at the children of the current node position
        for child in problem.getSuccessors(currentPosition):
            if(child[0] not in visited):
                print("child of pos: ", child[0])
                print("child direction: ", child[1])
                print("child cost: ", child[2])
                print("heuristic cost: ",(child[2] + heuristic(child[0], problem)))
                #create a new node with constructor
                newNode = Node(child[0], child[1],(child[2] + heuristic(child[0], problem)))
                #give the newNode the parent node
                newNode.parent = currentNode
                print("parent pos", newNode.parent.position)
                #push newNode to Queue
                priorityQueue.push(newNode, newNode.cost)
    
    while(currentNode.direction != None):
        #insert at the front of the list 
        finalPath.insert(0, currentNode.direction)
        #make currentNode = to the previous nodes parent and work up the list
        currentNode = currentNode.parent

    return finalPath


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
