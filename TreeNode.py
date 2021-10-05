from NeighborInfo import NeighborInfo
from State import State


class TreeNode:
    def __init__(self, state: State):
        # State
        self.state = state
        # Map state name to CostInfo
        self.neighbors = {}

    def __str__(self):
        res = "TreeNode of " + str(self.state) + ":\n"
        for n in self.neighbors:
            res += str(n)+": Driving: "+str(self.neighbors[n].drive_cost)+" Straight: "+str(self.neighbors[n].straight_cost)+"\n"
        res+="\n"
        return res

    def add_neighbor(self, name: str, drive_cost: int, straight_cost: int):
        self.neighbors[name] = (drive_cost, straight_cost)