import queue as Q
import Feature

class ChiSquare(object):

    def __init__(self, table, numberOfCat, index, cat):
        self.table = table
        self.cat = cat
        self.sum = 0
        self.numberOfCat = numberOfCat
        self.index = index

    def _setSum(self):
        self.sumVer = [0 for i in range(8)]
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
                k = []
                k.append(A)
                k.append(B)
                k.append(C)
                k.append(D)


                print(A,",",B,",",C,",",D)
                print((k[0]+k[2])*(k[1]+k[3])*(k[0]+k[1])*(k[2]+k[3]))

                CHI = (N * pow((A * D - C * B), 2)) / ((k[0]+k[2])*(k[1]+k[3])*(k[0]+k[1])*(k[2]+k[3]))

                if result[i] < CHI:
                    result[i] = CHI
                    result[i] = round(result[i], 3)

        queue = Q.PriorityQueue()
        for i in range(1, self.index):
            f = Feature.feature(result[i], i)
            queue.put(f)

        return queue




