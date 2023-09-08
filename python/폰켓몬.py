def solution(nums):
    numsLen = len(nums)/2
    numsSet = set(nums)
    if len(numsSet) >= numsLen:
        return numsLen
    else:
        return len(numsSet)