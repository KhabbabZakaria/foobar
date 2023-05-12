def solution(l):
    canDivides = []
    for i in range(len(l)):
        tmp = []
        for j in range(i+1, len(l)):
            if l[j]%l[i]==0:
                tmp.append(j)
        canDivides.append(tmp)  
    if len(canDivides)==0:
        return 0

    count = 0
    for i in range(len(canDivides)):
        if len(canDivides[i])==0:
            continue
        for element in canDivides[i]:
            nextTripletList = canDivides[element]
            if len(nextTripletList)==0:
                continue
            count += len(nextTripletList)
    return count



l = [1,1,1,1,1,1]
print(solution(l))

