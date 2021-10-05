class NeighborInfo:
    def __init__(self, drive_cost=0, straight_cost=0):
        self.drive_cost = drive_cost
        self.straight_cost = straight_cost

    def __str__(self):
        return str(self.drive_cost) + "," + str(self.straight_cost)