from State import State


class TreeNode:
    def __init__(self, state: State):
        self.state = state
        self.parent = None
        self.cost = float("inf")
        self.neighbors = {}

    def __str__(self):
        res = "TreeNode of " + str(self.state) + ":\n"
        if self.parent:
            res += "Parent: "+str(self.parent.state.initials) + "\n"
        res += "Cost: " + str(self.cost) + ":\n"
        res += str(self.neighbors)
        return res
