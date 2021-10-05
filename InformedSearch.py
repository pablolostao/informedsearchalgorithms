import timeit
from heapq import heappop,heappush


def greedy_best_first(origin, target, name_to_node, straight_distances):
    timeStart = timeit.default_timer()
    visited = set()
    path = []
    cost = 0
    cur = name_to_node[origin]
    while cur.state.initials != target:
        visited.add(cur.state.initials)
        path.append(cur.state.initials)
        minDistance = float("inf")
        node = None
        for neighbor in cur.neighbors:
            if neighbor not in visited and straight_distances[neighbor] < minDistance:
                minDistance = straight_distances[neighbor]
                node = name_to_node[neighbor]
        if node is None:
            print("Error, no candidates")
            exit()
        cost += cur.neighbors[node.state.initials].drive_cost
        cur = node
    path.append(target)
    timeEnd = timeit.default_timer()
    path_string = ""
    for state in path:
        path_string += state+" "
    res = '''
    Greedy Best First Search:
    Solution path: {path_string}
    Number of states on a path: {path_length}
    Path cost: {path_cost}
    Execution time: {elapsedTime}ms
    '''.format(path_string=path_string,path_length=len(path),
               path_cost=cost,elapsedTime=(timeEnd-timeStart)*1000)
    print(res)

def a_algorithm(origin, target, name_to_node, straight_distances):
    pq = []
    timeStart = timeit.default_timer()
    partial_path = {}
    partial_cost = {}
    visited = set()
    cur = name_to_node[origin]
    visited.add(cur.state.initials)
    partial_cost[cur.state.initials] = 0
    partial_path[cur.state.initials] = [cur.state.initials]
    while cur.state.initials != target:
        for neighbor in cur.neighbors:
            if neighbor not in visited:
                neighbor_cost = straight_distances[neighbor]+cur.neighbors[neighbor].drive_cost
                heappush(pq,(neighbor_cost,cur.state.initials,neighbor,cur.neighbors[neighbor].drive_cost))
                visited.add(neighbor)
        tup = heappop(pq)
        node = name_to_node[tup[2]]
        partial_cost[tup[2]] = partial_cost[tup[1]] + tup[3]
        partial_path[tup[2]] = partial_path[tup[1]].copy()
        partial_path[tup[2]].append(tup[2])
        if node is None:
            print("Error, no candidates")
            exit()
        cur = node
    timeEnd = timeit.default_timer()
    path_string = ""
    for state in partial_path[target]:
        path_string += state + " "
    res = '''
    A* Search:
    Solution path: {path_string}
    Number of states on a path: {path_length}
    Path cost: {path_cost}
    Execution time: {elapsedTime}ms
        '''.format(path_string=path_string, path_length=len(partial_path[target]),
                   path_cost=partial_cost[target], elapsedTime=(timeEnd - timeStart) * 1000)
    print(res)




