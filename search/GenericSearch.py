import util

def GenericSearchAlgorythm(problem, state, q, visited, parents, priority=False, heuristic=False):
	"""
	:param problem: The search problem we were given.
	:param state: The current state where our searcher is at.
	:param q: A Que method to store our next search moves.
	:param visited: Locations in the world where we already been or at least added to the Que.
	:param parents: The state and action that brought us to current location.
	:param priority: True if giving priority to points based on heuristic or a function.
	:param heuristic: True if giving priority based on heuristic (A* for example).
	:return: List of actions that would optimize our search problem
	"""
	if "numGoalStates" in problem.__dict__:
		prizes = 0
		finalPath = []
		while prizes < problem.numGoalStates:
			prizes += 1
			parents, newState = GoalSeeking(problem, state, q, [state], {}, priority, heuristic)
			finalPath.append(createPath(state, parents, newState))
			state = newState
			while not q.isEmpty():
				q.pop()
		return [item for sublist in finalPath for item in sublist]
	else:
		parents, newState = GoalSeeking(problem, state, q, visited, parents, priority, heuristic)
		return createPath(problem.getStartState() ,parents, newState)

def GoalSeeking(problem, state, q, visited, parents, priority, heuristic):
	while not problem.isGoalState(state):
		successors = problem.getSuccessors(state)
		for successor in successors:
			if not successor[0] in visited:
				if not priority:
					q.push(successor)
				else:
					if heuristic:
						q.push(successor,problem)
					else:
						q.push(successor, successor[2])
				visited.append(successor[0])
				parents[successor[0]] =(state,successor[1])
		if q.isEmpty():
			return util.raiseNotDefined()
		else:
			state = q.pop()[0]

	return parents, state

def createPath(startState, parents, endState):
	actions = []
	state = endState
	while state != startState:
		state, action = parents[state]
		actions.insert(0, action)
	return actions