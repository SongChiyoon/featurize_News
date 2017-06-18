class Feature(object):
    def __init__(self, weight, index):
        self.weight = weight
        self.index = index

    @property
    def getWeight(self):
        return self.weight

    def setNewindex(self, newIndex):
        self.newIndex = newIndex

    @property
    def getNewIndex(self):
        return self.newIndex

    @property
    def getIndex(self):
        return self.index


