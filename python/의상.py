from collections import Counter

def solution(clothes):
    types = []
    for i in clothes:
        types.append(i[1])
    clothesTypes = Counter(types)
    result = 1
    for i in clothesTypes:
        result *= clothesTypes[i] + 1
    return result - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))