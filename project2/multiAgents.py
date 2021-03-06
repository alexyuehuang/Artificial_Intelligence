# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


'''
Improve the ReflexAgent in multiAgents.py to play respectably.
The provided reflex agent code provides some helpful examples of methods that query the GameState for information.
A capable reflex agent will have to consider both food locations and ghost locations to perform well.
'''

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostPos = successorGameState.getGhostPositions()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    #ghostPositions = successorGameState.getGhostPosition()
    #getGhostPosition, might be helpdul

    #Closer to the closest pellet,  closer to the
    #Use the next state - current state.
    #find the closest pellet and the ghost
    #find the closest ghost that was not scared

    '''
    Things you have to consider:
    1. Closest Pellet/Capsule/Scared Ghost
    2. Closest Non-scared ghost

    '''



    "*** YOUR CODE HERE ***"
    "*** YOUR CODE HERE ***"
    # With help from TA, telling me that ghosts can propel the Pacmen.
    closest_food = (0,0)
    smallest_food_distance = 511
    # Find the closest food/pellet/etc.


    # Find closest
    newFoodList = newFood.asList()
    #Cloest Food point
    for foodPoint in range(0,len(newFoodList)):
      if manhattanDistance(newFoodList[foodPoint],newPos) < smallest_food_distance:
        closest_food = newFoodList[foodPoint]
        smallest_food_distance = manhattanDistance(newFoodList[foodPoint],newPos)

    closest_ghost = (0,0)
    smallest_ghost_distance = 800
    # Closest Ghost
    for ghostPos in newGhostPos:
          if manhattanDistance(ghostPos,newPos) < smallest_ghost_distance:
            closest_ghost = ghostPos
            smallest_ghost_distance = manhattanDistance(ghostPos,newPos)


    #Eliminate Scared Ghosts. I just don't want to screw it up.
    scaredGhosts_total = 0
    for i  in newScaredTimes:
      if newScaredTimes ==0:
        scaredGhosts_total += 1

    #print(closest_food)
    #print(closest_ghost)

    #print ("Done for this round.")
    #print(currentGameState.getScore())
    #print (action)
    if smallest_ghost_distance < 5:
        return successorGameState.getScore()+(len(newGhostPos)-scaredGhosts_total)*(smallest_ghost_distance)/((smallest_food_distance+1)*(len(newFoodList)+1))
    else:
        return successorGameState.getScore()+(len(newGhostPos)-scaredGhosts_total)*(smallest_ghost_distance)/((smallest_food_distance+1)*(len(newFoodList)+1))

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent (question 2)
  """
  def MinRecursion(self,gameState, level ,i,isMin):
    if False==isMin:
        if level ==self.depth+1:
            return self.evaluationFunction(gameState)
        maxValue=float('-inf')
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0,action)
            q=self.MinRecursion(newState, level, 1, True)
            if q>maxValue:
                maxValue=q
        return maxValue
    minValue =float('inf')
    if i==gameState.getNumAgents()-1:
        if gameState.getLegalActions(i)==[]:
            return self.evaluationFunction(gameState)
        for action in gameState.getLegalActions(i):
            nextState = gameState.generateSuccessor(i, action)
            q=self.MinRecursion(nextState, level+1,0,False)
            if minValue>q:
                minValue=q
        return minValue
    if gameState.getLegalActions(i)==[]:
        return self.evaluationFunction(gameState)
    for action in gameState.getLegalActions(i):
        nextState=gameState.generateSuccessor(i,action)
        q=self.MinRecursion(nextState, level, i+1, True)
        if minValue>q:
            minValue=q
    return minValue

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game
    """
    "*** YOUR CODE HERE ***"
    maxValue =float('-inf')
    maxAction=Directions.STOP
    for action in gameState.getLegalActions(0):
        newState = gameState.generateSuccessor(0,action)
        q=self.MinRecursion(newState,1,1, True)
        if maxValue<q:
            maxValue=q
            maxAction= action
    print(maxValue)
    return maxAction




class AlphaBetaAgent(MultiAgentSearchAgent):
  """
    Your minimax agent with alpha-beta pruning (question 3)
  """
  def MinRecursion(self,gameState, level ,i,isMin, alpha, beta):
    if False==isMin:
        if level ==self.depth+1:
            return self.evaluationFunction(gameState)
        maxValue=float('-inf')
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0,action)
            q=self.MinRecursion(newState, level, 1, True, alpha, beta)
            maxValue = max(maxValue, q)
            if q>maxValue:
                maxValue=q
            if maxValue>=beta:
                return maxValue
            alpha = max(alpha, maxValue)
        return maxValue
    minValue =float('inf')
    if i==gameState.getNumAgents()-1:
        if gameState.getLegalActions(i)==[]:
            return self.evaluationFunction(gameState)
        for action in gameState.getLegalActions(i):
            nextState = gameState.generateSuccessor(i, action)
            q=self.MinRecursion(nextState, level+1,0,False, alpha, beta)
            minValue=min(minValue, q)
            if minValue>q:
                minValue=q
            if minValue<=alpha:
                return minValue
            beta = min(beta, minValue)
        return minValue
    if gameState.getLegalActions(i)==[]:
        return self.evaluationFunction(gameState)
    for action in gameState.getLegalActions(i):
        nextState=gameState.generateSuccessor(i,action)
        q=self.MinRecursion(nextState, level, i+1, True, alpha, beta)
        minValue=min(minValue, q)
        if minValue>q:
            minValue=q
        if minValue<=alpha:
            return minValue
        beta = min(beta, minValue)
    return minValue

  def getAction(self, gameState):
    """
      Returns the minimax action using self.depth and self.evaluationFunction
    """
    "*** YOUR CODE HERE ***"
    maxValue =float('-inf')
    maxAction=Directions.STOP
    for action in gameState.getLegalActions(0):
        newState = gameState.generateSuccessor(0,action)
        q=self.MinRecursion(newState,1,1, True, float('-inf'), float('inf'))
        if maxValue<q:
            maxValue=q
            maxAction= action
    print(maxValue)
    return maxAction

class ExpectimaxAgent(MultiAgentSearchAgent):
  """
    Your expectimax agent (question 4)
  """
  def MinRecursion(self,gameState, level ,i,isMin):
    if False==isMin:
        if level ==self.depth+1:
            return self.evaluationFunction(gameState)
        maxValue=float('-inf')
        for action in gameState.getLegalActions(0):
            newState = gameState.generateSuccessor(0,action)
            q=self.MinRecursion(newState, level, 1, True)
            if q>maxValue:
                maxValue=q
        return maxValue
    meanValue = 0
    if i==gameState.getNumAgents()-1:
        if gameState.getLegalActions(i)==[]:
            return self.evaluationFunction(gameState)
        leng=len(gameState.getLegalActions(i));
        for action in gameState.getLegalActions(i):
            nextState = gameState.generateSuccessor(i, action)
            q=self.MinRecursion(nextState, level+1,0,False)
            meanValue+=q/leng
        return meanValue
    if gameState.getLegalActions(i)==[]:
        return self.evaluationFunction(gameState)
    leng = len(gameState.getLegalActions(i));
    for action in gameState.getLegalActions(i):
        nextState=gameState.generateSuccessor(i,action)
        q=self.MinRecursion(nextState, level, i+1, True)
        meanValue+=q/leng
    return meanValue

  def getAction(self, gameState):
    """
      Returns the expectimax action using self.depth and self.evaluationFunction

      All ghosts should be modeled as choosing uniformly at random from their
      legal moves.
    """
    "*** YOUR CODE HERE ***"
    maxValue =float('-inf')
    maxAction=Directions.STOP
    for action in gameState.getLegalActions(0):
        newState = gameState.generateSuccessor(0,action)
        q=self.MinRecursion(newState,1,1, True)
        if maxValue<q:
            maxValue=q
            maxAction= action
    print(maxValue)
    return maxAction

def betterEvaluationFunction(currentGameState):
  """
    Your extreme ghost-hunting, pellet-nabbing, food-gobbling, unstoppable
    evaluation function (question 5).

    DESCRIPTION: <write something here so we know what you did>
  """
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

# Abbreviation
better = betterEvaluationFunction

class ContestAgent(MultiAgentSearchAgent):
  """
    Your agent for the mini-contest
  """

  def getAction(self, gameState):
    """
      Returns an action.  You can use any method you want and search to any depth you want.
      Just remember that the mini-contest is timed, so you have to trade off speed and computation.

      Ghosts don't behave randomly anymore, but they aren't perfect either -- they'll usually
      just make a beeline straight towards Pacman (or away from him if they're scared!)
    """
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()
