def solution(participant, completion):
    runners = participant
    completionRunners = completion
    runners.sort()
    completionRunners.sort()
    for i in range(0, len(completionRunners)):
        if runners[i] != completionRunners[i]:
            return runners[i]
    return runners[-1]

print(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]))
