from simpleai.search import SearchProblem, astar

GOAL = 'HELLO WORLD'

class HelloProblem(SearchProblem):
    def actions(self, state):
        return list(' ABCDEFGHIJKLMNOPQRSTUVWXYZ') if len(state) < len(GOAL) else []

    def result(self, state, action):
        return state + action

    def is_goal(self, state):
        return state == GOAL

    def heuristic(self, state):
        return sum([1 if state[i] != GOAL[i] else 0 for i in range(len(state))]) + (len(GOAL) - len(state))

problem = HelloProblem(initial_state='')
result = astar(problem)

print("Final State:", result.state)

# Corrected the path reconstruction
path = [node.state for node in result.path()]
print("Path to Goal:", path)
