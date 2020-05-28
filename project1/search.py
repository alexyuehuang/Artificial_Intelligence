# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called
by Pacman agents (in searchAgents.py).
"""

import util
import copy

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples,
        (successor, action, stepCost), where 'successor' is a
        successor to the current state, 'action' is the action
        required to get there, and 'stepCost' is the incremental
        cost of expanding to that successor
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.  The sequence must
        be composed of legal moves
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other
    maze, the sequence of moves will be incorrect, so only use this for tinyMaze
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s,s,w,s,w,w,s,w]

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first
    [2nd Edition: p 75, 3rd Edition: p 87]

    Your search algorithm needs to return a list of actions that reaches
    the goal.  Make sure to implement a graph search algorithm
    [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    value = problem.getStartState()
    result = dfSearch(value, problem, [])
    result.reverse()
    return result

def dfSearch(state, problem, discovered):
    discovered.append(state)
    for successor in problem.getSuccessors(state):
        if successor[0] in discovered:
            continue
        if problem.isGoalState(successor[0]):
            return [successor[1]]
        answer =dfSearch(successor[0], problem, discovered)
        if answer!=[]:
            answer.append(successor[1])
            #print successor
            return answer
    return []

"""
Connects all paths from breadth first search.
"""
def connectPaths(smallpath):
    outpath = []
    for i in range(1,len(smallpath)):
        if(smallpath[i][1]>smallpath[i-1][1]):
            outpath.append( 'North')
        elif(smallpath[i][1]<smallpath[i-1][1]):
            outpath.append( 'South')
        elif(smallpath[i][0]>smallpath[i-1][0]):
            outpath.append( 'East')
        else:
            outpath.append( 'West'  )

    return outpath

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first.
    [2nd Edition: p 73, 3rd Edition: p 82]
    """
    "*** YOUR CODE HERE ***"
    """
    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """

    # Construct a tuple that contains two things: the current node, and the current path.
    #path = []
    #Seems the only way to remember a path is to give a tuple and deal with it.
    #Received help from Sherry Shi, on how to memorize paths in theory.
    #Code is constructed hours after help.
    queue = util.Queue() # use queue to represent the existence of fringe.
    queue.push((problem.getStartState(),[],[]))# The start value is a tuple (a,b)
    closed = set()


    while not queue.isEmpty():
        pop1 = queue.pop()
        if problem.isGoalState(pop1[0]):
            return pop1[2]#connectPaths(pop1[1])
        if pop1[0] not in closed:
            closed.add(pop1[0])
            new_successors = [successor for successor in problem.getSuccessors(pop1[0])]
            for new_success in new_successors:
                list2 = copy.deepcopy(pop1[2])
                list2.append(new_success[1])
                queue.push((new_success[0],[],list2))

    return ((0,0),[(0,0)])

    #util.raiseNotDefined()



def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"
    pq = util.PriorityQueue()
    # Should be similar to BFS?

    #push, pop, isEmpty

    pq.push((problem.getStartState(),[],0,[]),0)# The start value is a tuple (a,b) #should it be 0? I mean the priority...
    closed = set()
    #Whole structure
    #For pq.push: (((x,y),listOfDots,totalcost,listOfDirections),cost)
    #For pop1:
    #[0]     [1]       [2]'
    #For ((a,b),[List],priority,[ListOfDirections])
    #For getSuccessor:

    #((a,b),'Direction',cost)
    while not pq.isEmpty():
        pop1 = pq.pop()
        pop1[1].append(pop1[0])
        if problem.isGoalState(pop1[0]):
            return pop1[3]#connectPaths(pop1[1])
        if pop1[0] not in closed:
            closed.add(pop1[0])
            new_successors = [successor for successor in problem.getSuccessors(pop1[0])]
            for new_success in new_successors:
                list3 = copy.deepcopy(pop1[3])
                list3.append(new_success[1])
                list2 = copy.deepcopy(pop1[1])
                pq.push((new_success[0],list2,new_success[2]+pop1[2],list3),new_success[2]+pop1[2])

    return ((0,0),[(0,0)])
'''
    #util.raiseNotDefined()
        while not pq.isEmpty():
            pop1 = pq.pop()
        #print pop1[1]
        pop1[1].append(pop1[0])
        if problem.isGoalState(pop1[0]):
            #print pop1[1]
            #print pop1[1]
            return connectPaths(pop1[1])
        if pop1[0] not in closed:
            closed.add(pop1[0])
            new_successors = [successor for successor in problem.getSuccessors(pop1[0])]
            for new_success in new_successors:
                list3
                #print new_success
                list2 = copy.deepcopy(pop1[1])
                #print pop1[2]
                pq.push((new_success[0],list2,new_success[2]+pop1[2]),new_success[2]+pop1[2])

    return ((0,0),[(0,0)])
'''

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()


    pq = util.PriorityQueue()
    # Should be similar to BFS?

    #push, pop, isEmpty

    pq.push((problem.getStartState(),[],0,[]),0)# The start value is a tuple (a,b) #should it be 0? I mean the priority...
    closed = set()
    #Whole structure
    #For pq.push: (((x,y),listOfDots,totalcost,listOfDirections),cost)
    #For pop1:
    #[0]     [1]       [2]'
    #For ((a,b),[List],priority,[ListOfDirections])
    #For getSuccessor:

    #((a,b),'Direction',cost)
    while not pq.isEmpty():
        pop1 = pq.pop()
        pop1[1].append(pop1[0])
        if problem.isGoalState(pop1[0]):
            return pop1[3]#connectPaths(pop1[1])
        if pop1[0] not in closed:
            closed.add(pop1[0])
            new_successors = [successor for successor in problem.getSuccessors(pop1[0])]
            for new_success in new_successors:
                list3 = copy.deepcopy(pop1[3])
                list3.append(new_success[1])
                list2 = copy.deepcopy(pop1[1])
                pq.push((new_success[0],list2,new_success[2]+pop1[2],list3),new_success[2]+pop1[2]+heuristic(new_success[0],problem))

    return ((0,0),[(0,0)])


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
