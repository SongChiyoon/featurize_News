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
        print(category, ":",feature)

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
        if feature in map.keys():
            return map[feature]
        else:
            return self.index

    #use konlp libray
    def split(self, text):
        kkma = Kkma()
        feature = kkma.nouns(text)
        return feature
#skip blank line
def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

kkma = Kkma()

fileName = []
for i in range(5):
    fileName.append("data/HKIB-20000_00" +str(i+1)+ ".txt")
    print(fileName[i])
map = {}
map["건강과 의학"] =  0
map["경제"] = 1
map["과학"] = 2
map["교육"] = 3
map["문화와 종교"] = 4
map["사회"] = 5
map["산업"] = 6
map["여가생활"] = 7

count = [0] * 8
skip = False
makeTable = mapTable()
cat = -1

news = ""
numberOfCat = [0 for i in range(8)]

for T in range(4):
    with open(fileName[T], 'r') as f:
        for line in nonblank_lines(f):
            if "@DOCUMENT" in line:
                if news != "":
                    result = makeTable.split(news)
                    for feature in result:
                        if feature.isdigit():
                            continue
                        makeTable.addCount(category=cat, feature=feature)
                    news = ""

                ne = next(f)
                ne = next(f)
                cat = ne.split('/')[1]
                cat = map[cat]
                numberOfCat[cat] += 1
                print(T,":",cat)
                ne = next(f)
                ne = next(f)
                ne = next(f)

            else:
                news += line

table = makeTable.getTable()



