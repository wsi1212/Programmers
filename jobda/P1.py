def solution(N, W):
    start = [0] * 26
    end = [0] * 26
    diff = [0] * 26
    isAllOfLenOne = True
    for i in W:
        if len(i) != 1:
            isAllOfLenOne = False
        start[ord(i[0]) - 97] += 1
        end[ord(i[-1]) - 97] += 1
    for i in range(0, 26):
        diff[i] = start[i] - end[i]
    alphabet = set()
    for i in range(0, 26):
        if 1 in alphabet and start[i] - end[i] == 1:
            return ["impossible"]
        alphabet.add(start[i] - end[i])
    if isAllOfLenOne:
        temp = W[0]
        for i in W:
            if i != temp:
                return ["impossible"]
        return W
    if len(alphabet) == 1:
        return sorted(W)
    elif 1 in alphabet and -1 in alphabet and 0 in alphabet and len(alphabet) == 3:
        try:
            startedAlphbot = chr(diff.index(1) + 97)
            for i in W:
                if startedAlphbot == i[0]:
                    return [i]
        except ValueError:
            try:
                startedAlphbot = chr(diff.index(-1) + 97)
                for i in W:
                    if startedAlphbot == i[0]:
                        return [i]
            except ValueError:
                return ["impossible"]
    else:
        return ["impossible"]

print(solution(5, ["abcd", "defga", "ddddh"]))