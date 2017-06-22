import queue as Q
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

    def __cmp__(self, other):
        if self.weight > other.weight:
            return 1
        elif self.weight < other.weight:
            return -1
        else:
            return 0


class chiSquare(object):

    def __init__(self, table, numberOfCat, index, cat):
        self.table = table
        self.cat = cat
        self.sum = 0
        self.numberOfCat = numberOfCat
        self.index = index

    def _setSum(self):
        self.sumVer = [0 for i in range(self.numberOfCat)]
        self.sumHor = [0 for i in range(self.index)]
        for c in range(self.cat):
            self.sum += self.numberOfCat[c]
            for i in range(1, self.index):
                self.sumVer[c] += self.table[i][c]
                self.sumHor[i] += self.table[i][c]

    def chiResult(self):
        self._setSum()

        #chisquare expression
        N = 15978
        result = [0 for i in range(self.index)]

        for i in range(1, self.index):
            for c in range(self.cat):
                A = self.table[i][c]
                B = self.numberOfCat[c] - A
                C = self.sumHor[i] - A
                D = self.sum - (A+B+C)
                k = [A,B,C,D]

                if A < 0 or B < 0 or C < 0 or D < 0:
                    print(A,",",B,",",C,",",D)

                CHI = (N * pow((A * D - C * B), 2)) / ((k[0]+k[2])*(k[1]+k[3])*(k[0]+k[1])*(k[2]+k[3]))

                if result[i] < CHI:
                    result[i] = CHI
                    result[i] = round(result[i], 3)

        queue = Q.PriorityQueue()
        for i in range(1, self.index):
            f = Feature(result[i], i)
            queue.put(f)
            
        return queue




