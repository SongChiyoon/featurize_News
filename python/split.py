from konlpy.tag import Kkma
kkma = Kkma()
list = kkma.nouns('대학에서 DB, 통계학, 이산수학, 이산수학 등을 배웠지만')
print(list)