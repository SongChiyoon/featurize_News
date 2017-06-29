from konlpy.tag import Kkma
import chiSquare
import mapTable

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
makeTable = mapTable.mapTable()
cat = -1

news = ""
numberOfCat = [0 for i in range(8)]
ck = 0
for T in range(1):
    with open(fileName[T], 'r') as f:
    #with open("data/test.txt", 'r') as f:
        for line in nonblank_lines(f):
            if "@DOCUMENT" in line:
                if news != "":
                    result = makeTable.split(news)
                    for feature in result:
                        featureLength = len(feature)
                        if feature.isdigit() :
                            continue
                        if  featureLength >= 2 and featureLength <= 5:
                            makeTable.addCount(category=cat, feature=feature)
                    print(ck)
                    ck += 1
                    news = ""

                ne = next(f)
                ne = next(f)
                cat = ne.split('/')[1]
                cat = map[cat]
                numberOfCat[cat] += 1
               # print(T,":",cat)
                ne = next(f)
                ne = next(f)
                ne = next(f)

            else:
                news += line

table = makeTable.getTable()

m = makeTable.getMap()
index = makeTable.getIndex()
chi = chiSquare.ChiSquare(table=table,numberOfCat = numberOfCat,index=index, cat = 8)
chiQueue = chi.chiResult()
resultMap = {}
features = []
newIndex = 0

f = open("check.txt","w")
for i in (1, index):
    f.write("index : %d (%s)"%(i, m[i]))
print(table)
'''
while not chiQueue.empty():
    f = chiQueue.get()
    f.setNewIndex(newIndex)
    features.append(f)
    resultMap[m[f.getIndex]] = newIndex
    print(m[f.getIndex], ":",f.getWeight,"여기야")
    newIndex += 1'''