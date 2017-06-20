from konlpy.tag import Kkma
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

for T in range(1):
    f = open(fileName[T], 'r')
    for line in f:
        if "<KW>" in line:
            print(line)
            for skip in f:
                if "@" in skip:
                    print(skip + 'find')

        #list = kkma.nouns(line)
        #print(list)
