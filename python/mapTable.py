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

    def _addCount(self, category, feature):
        position = self._getIndex(feature)
        if position == self.index:
            self.table[category][position] = 1
            self.map[feature] =  position
            self.Index2String[position] = feature
            self.index += 1
        else:
            self.table[category][position] += 1

    def _getIndex(self, feature):
        if feature in map.keys():
            return map[feature]
        else:
            return self.index

    #use konlp libray
    def split(self, category, text):
        kkma = Kkma()
        feature = kkma.nouns(text)
        return feature

map = {1 : 'song'}
table = [[0] * 8 for i in range(20)]
print(table)
id = 2
if id in map.keys():
    print(map[id])
else:
    print("no")
