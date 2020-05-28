# valueIterationAgents.py
# -----------------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
  """
      * Please read learningAgents.py before reading this.*

      A ValueIterationAgent takes a Markov decision process
      (see mdp.py) on initialization and runs value iteration
      for a given number of iterations using the supplied
      discount factor.
  """
  def __init__(self, mdp, discount = 0.9, iterations = 100):
    """
      Your value iteration agent should take an mdp on
      construction, run the indicated number of iterations
      and then act according to the resulting policy.
    
      Some useful mdp methods you will use:
          mdp.getStates()
          mdp.getPossibleActions(state)
          mdp.getTransitionStatesAndProbs(state, action)
          mdp.getReward(state, action, nextState)
    """
    self.mdp = mdp
    self.discount = discount
    self.iterations = iterations
    self.values = util.Counter() # A Counter is a dict with default 0
     
    "*** YOUR CODE HERE ***"
    
    for i in range(0,iterations):
        self.newValues =util.Counter()
        self.newValues=util.Counter.copy(self.values)
        for state in self.mdp.getStates():
            if str(state)=='TERMINAL_STATE':
                self.newValues[state]=self.getValue(state)
                continue
            if self.getValue(state)==-1:
                self.newValues[state]=self.getValue(state)
                continue
            array_for_largest_values = []
            for action in self.mdp.getPossibleActions(state):
                array_for_largest_values.append(self.getQValue(state,action))
                 #print(self.getQValue(state,action))
            self.newValues[state] = max(array_for_largest_values)
        self.values=util.Counter.copy(self.newValues)
    
  def getValue(self, state):
    """
      Return the value of the state (computed in __init__).
    """
    return self.values[state]


  def getQValue(self, state, action):
    """
      The q-value of the state action pair
      (after the indicated number of value iteration
      passes).  Note that value iteration does not
      necessarily create this quantity and you may have
      to derive it on the fly.
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    allPossibleActions = self.mdp.getPossibleActions(state)

     #mdp.getTransitionStatesAndProbs(state, action)
    allTransistionAndActionPairs = self.mdp.getTransitionStatesAndProbs(state, action)
     #Adding all the things up.
    sum_N = 0 # Accumulate all values.
    for realTransistionAndPair in  allTransistionAndActionPairs: #[0]:state, #1:prob
        sum_N += realTransistionAndPair[1]*(self.mdp.getReward(state, action, realTransistionAndPair[0])+(self.discount)*self.values[realTransistionAndPair[0]])
           
    return sum_N

    
  def getPolicy(self, state):
    """
      The policy is the best action in the given state
      according to the values computed by value iteration.
      You may break ties any way you see fit.  Note that if
      there are no legal actions, which is the case at the
      terminal state, you should return None.
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    
    
    if(str(state)=='TERMINAL_STATE'):
           return None
    else:
     #Do something here reasonable.
        array = dict()
        number_array = []
        for realAction in self.mdp.getPossibleActions(state):
            array[self.getQValue( state, realAction)] = realAction
            number_array.append(self.getQValue( state, realAction))
        return array[max(number_array)]


  def getAction(self, state):
    "Returns the policy at the state (no exploration)."
    return self.getPolicy(state)
  
