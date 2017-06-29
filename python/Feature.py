class feature(object):
    def __init__(self, weight, index):
        self.weight = weight
        self.index = index

    @property
    def getWeight(self):
        return self.weight

    def setNewIndex(self, newIndex):
        self.newIndex = newIndex

    @property
    def getNewIndex(self):
        return self.newIndex

    @property
    def getIndex(self):
        return self.index

    def __cmp__(self, other):
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0

