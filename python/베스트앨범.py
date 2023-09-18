def swapPositions(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def solution(genres, plays):
    answer = []
    music = []
    musicPlaysDict = {}
    for i in range(0, len(genres)):
        music.append([genres[i], plays[i]])
    for i in range(0, len(genres)):
        musicPlaysDict[genres[i]] = 0
    for i in range(0, len(genres)):
        musicPlaysDict[genres[i]] += plays[i]
    sortedMusicDict = sorted(musicPlaysDict.items(), key=lambda x: x[1])
    sortedMusitType = []
    for i in sortedMusicDict:
        sortedMusitType.append(i[0])
    for i in sortedMusitType:
        topTwoMaxPlayTemp = []
        for j in range(0, len(music)):
            if music[j][0] == i:
                topTwoMaxPlayTemp.append([music[j][1], j])
        for j in range(0, len(topTwoMaxPlayTemp)):
            for n in range(0, len(topTwoMaxPlayTemp)):
                if j != n and topTwoMaxPlayTemp[j][0] < topTwoMaxPlayTemp[n][0]:
                    swapPositions(topTwoMaxPlayTemp, j, n)
                elif topTwoMaxPlayTemp[j][0] == topTwoMaxPlayTemp[n][0] and topTwoMaxPlayTemp[n][1] < topTwoMaxPlayTemp[j][1]:
                    swapPositions(topTwoMaxPlayTemp, j, n)
        if (len(topTwoMaxPlayTemp) >= 2):
            for j in topTwoMaxPlayTemp[-2:]:
                answer.append(j[1])
        else:
            answer.append(topTwoMaxPlayTemp[0][1])
    answer.reverse()
    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [800, 600, 150, 800, 2000]))
