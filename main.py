import sys

from InformedSearch import greedy_best_first, a_algorithm
from NeighborInfo import NeighborInfo
from State import State
from TreeNode import TreeNode


def main():
    # If the input does not have two arguments, exit
    args = sys.argv[1:]
    if len(args) != 2:
        print("ERROR: Not enough or too many input arguments.")
        exit()
    # Map string-TreeNode (from state name to TreeNode)
    name_to_node = {}
    # Straight distances from each state to the target. Map string-int (state name to distance)
    straight_distances = {}
    # This function fills both structures above
    _create_name_to_node_from_csv(name_to_node, straight_distances, args[1])
    greedy_best_first(args[0], args[1], name_to_node, straight_distances)
    a_algorithm(args[0], args[1], name_to_node, straight_distances)


# Fills two maps passed as inputs. State name to TreeNode and state name to distance to the target.
# The third input is the target name
def _create_name_to_node_from_csv(name_to_node, straight_distances, target):
    states_order = None
    # Read the first file and create structure
    driving = open('driving.csv')
    for i, row in enumerate(driving):
        if i == 0:
            states_order = row.split(",")[1:]
            states_order[-1] = states_order[-1][:-1]
            continue
        name = states_order[i - 1]
        state = State(name)
        name_to_node[name] = TreeNode(state)
        data = row.split(",")
        data[-1] = data[-1][:-1]
        for j in range(1, len(data)):
            value = int(data[j])
            if value in [0, -1]:
                continue
            cost_info = NeighborInfo(value)
            name_to_node[name].neighbors[states_order[j - 1]] = cost_info
    driving.close()
    straight = open('straightline.csv')
    for i, row in enumerate(straight):
        if i == 0 or i > len(states_order):
            continue
        data = row.split(",")
        data[-1] = data[-1][:-1]
        name = states_order[i - 1]
        for j in range(1, len(states_order) + 1):
            if name == target:
                straight_distances[states_order[j - 1]] = int(data[j])
            if states_order[j - 1] not in name_to_node[name].neighbors:
                continue
            name_to_node[name].neighbors[states_order[j - 1]].straight_cost = int(data[j])
    straight.close()


if __name__ == "__main__":
    main()
