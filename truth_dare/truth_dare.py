testCases = int(input())
result = []
for i in range(testCases):
    res = 0
    tR = int(input())
    tRList = list(input().split())
    dR = int(input())
    dRList = list(input().split())
    tS = int(input())
    tSList = list(input().split())
    dS = int(input())
    dSList = list(input().split())
    for j in tSList:
        if j in tRList:
            continue
        else:
            res = 1
            break
    if res == 0:
        for j in dSList:
            if j in dRList:
                continue
            else:
                res = 1
                break
    if res == 0:
        print('yes')
    else :
        print('no')
