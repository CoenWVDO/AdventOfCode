#input is 652601
n = 652601

scores = [3,7]
indexElfA = 0
indexElfB = 1

"""
while len(scores) <  n+10:
    digitStr = str(scores[indexElfA] + scores[indexElfB])
    scores.extend(map(int, digitStr))
    indexElfA += scores[indexElfA] + 1
    indexElfA %= len(scores)
    indexElfB += scores[indexElfB] + 1
    indexElfB %= len(scores)

print("".join([str(y) for y in scores[n:n+10]]))
"""

#part 2:
scores = [3,7]
indexElfA = 0
indexElfB = 1

bla = [int(k) for k in str(n)]
st = str(n)
count = 0
while scores[-len(st):] != bla:
    count+=1
    digitStr = str(scores[indexElfA] + scores[indexElfB])
    scores.extend(map(int, digitStr))
    indexElfA += scores[indexElfA] + 1
    indexElfA %= len(scores)
    indexElfB += scores[indexElfB] + 1
    indexElfB %= len(scores)
    if scores[-len(st):] == bla or scores[-len(st)-1:-1] == bla:
        break
        
if scores[-len(st):] == bla:
    print(len(scores) - len(st))
else:
    print(len(scores) - len(st) - 1)
