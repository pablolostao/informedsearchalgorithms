import timeit
from heapq import heappop, heappush

from State import State
from TreeNode import TreeNode

STRING_TO_RETURN = '''
    {algorithm}:
    Solution path: {path_string}
    Number of states on a path: {path_length}
    Path cost: {path_cost}
    Execution time: {elapsedTime} seconds
    '''

def greedy_best_first(origin, target, name_to_neighbors, straight_distances):
    timeStart = timeit.default_timer()
    state = State(origin)
    node = TreeNode(state)
    node.neighbors = name_to_neighbors[origin]
    node.cost = 0
    frontier = [[straight_distances[origin],origin,node]]
    reached = {origin:node}
    finished = False
    while frontier:
        node = heappop(frontier)[2]
        if node.state.initials == target:
            finished = True
            break
        for neighbor in node.neighbors:
            if neighbor not in reached or node.cost + node.neighbors[neighbor] < reached[neighbor].cost:
                if neighbor not in reached:
                    new_state = State(neighbor)
                    reached[neighbor] = TreeNode(new_state)
                    reached[neighbor].cost = node.cost + node.neighbors[neighbor]
                    reached[neighbor].neighbors = name_to_neighbors[neighbor]
                reached[neighbor].cost = node.cost + node.neighbors[neighbor]
                reached[neighbor].parent = node
                heappush(frontier, [straight_distances[neighbor],neighbor,reached[neighbor]])
    timeEnd = timeit.default_timer()
    if not finished:
        return STRING_TO_RETURN.format(algorithm="Greedy Best First Search",path_string="FAILURE: NO PATH FOUND",
                                       path_length=0,path_cost=0,elapsedTime=(timeEnd-timeStart))
    cost = node.cost
    path_string = node.state.initials
    length = 1
    while node.parent:
        length += 1
        node = node.parent
        path_string = node.state.initials+" "+path_string

    return STRING_TO_RETURN.format(algorithm="Greedy Best First Search",path_string=path_string,path_length=length,
                                   path_cost=cost,elapsedTime=(timeEnd-timeStart))


def a_algorithm(origin, target, name_to_neighbors, straight_distances):
    timeStart = timeit.default_timer()
    state = State(origin)
    node = TreeNode(state)
    node.neighbors = name_to_neighbors[origin]
    node.cost = 0
    frontier = [[straight_distances[origin],origin,node]]
    reached = {origin:node}
    finished = False
    while frontier:
        node = heappop(frontier)[2]
        if node.state.initials == target:
            finished = True
            break
        for neighbor in node.neighbors:
            if neighbor not in reached or node.cost + node.neighbors[neighbor] < reached[neighbor].cost:
                if neighbor not in reached:
                    new_state = State(neighbor)
                    reached[neighbor] = TreeNode(new_state)
                    reached[neighbor].cost = node.cost + node.neighbors[neighbor]
                    reached[neighbor].neighbors = name_to_neighbors[neighbor]
                reached[neighbor].cost = node.cost + node.neighbors[neighbor]
                reached[neighbor].parent = node
                heappush(frontier, [reached[neighbor].cost+straight_distances[neighbor],neighbor,reached[neighbor]])
    timeEnd = timeit.default_timer()
    if not finished:
        return STRING_TO_RETURN.format(algorithm="A* Search",path_string="FAILURE: NO PATH FOUND",
                                       path_length=0,path_cost=0,elapsedTime=(timeEnd-timeStart))
    cost = node.cost
    path_string = node.state.initials
    length = 1
    while node.parent:
        length += 1
        node = node.parent
        path_string = node.state.initials+" "+path_string

    return STRING_TO_RETURN.format(algorithm="A* Search",path_string=path_string,path_length=length,
                                   path_cost=cost,elapsedTime=(timeEnd-timeStart))