import util

def GenericSearchAlgorythm(problem, state, q, visited, parents):
	"""
	:param problem: The search problem we were given.
	:param state: The current state where our searcher is at.
	:param q: A Que method to store our next search moves.
	:param visited: Locations in the world where we already been or at least added to the Que.
	:param parents: The state and action that brought us to current location.
	:return: List of actions that would optimize our search problem
	"""
	while not problem.isGoalState(state):
		successors = problem.getSuccessors(state)
		if len(successors) == 1:
			#TrimPath()
			print("told ya")
			pass
		else:
			for successor in successors:
				if not successor[0] in visited:
					q.push(successor)
					visited.append(successor[0])
					parents[successor[0]] =(state,successor[1])
		if q.isEmpty():
			return util.raiseNotDefined()
		else:
			state = q.pop()[0]
			print("state is: ", state)

	actions=[]
	while state != problem.getStartState():
		state,action = parents[state]
		actions.insert(0,action)
	return actions

def TrimPath():
	pass
#print(GenericSearchAlgorythm(1,2,3,4,5))