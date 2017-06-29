from konlpy.tag import Kkma
class mapTable(object):

    def __init__(self):
        self.kkma = Kkma()
        self.table = [[0] * 8 for i in range(10000000)]
        self.index = 0
        self.map = {}
        self.Index2String = {}

    def getMap(self):
        return self.map

    def getTable(self):
        return self.table

    def addCount(self, category, feature):
        position = self._getIndex(feature)
        #print(category, ":",feature)

        if position == self.index:
            self.table[position][category] = 1
            self.map[feature] =  position
            self.Index2String[position] = feature
            self.index += 1
        else:
            self.table[position][category] += 1

    def getIndex(self):
        return self.index

    def _getIndex(self, feature):
        if feature in self.map.keys():
            return self.map[feature]
        else:
            return self.index

    #use konlp libray
    def split(self, text):
        kkma = Kkma()
        feature = kkma.nouns(text)
        return feature