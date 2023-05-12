def solution(n):
    count = 0
    integer = int(n)
    if integer == 1:
        return count
    countList = [count]
    graph = [integer]
    soFar = []
    while len(graph)>0:
        poppedGraph = graph.pop(0)
        poppedCount = countList.pop(0)
        if poppedGraph in soFar:
            continue
        soFar.append(poppedGraph)
        if poppedGraph==1:
            return poppedCount
        if poppedGraph%2==0:
            graph.append(poppedGraph//2)
            countList.append(poppedCount+1)
        else:
            graph.append(poppedGraph+1)
            countList.append(poppedCount+1)
            graph.append(poppedGraph-1)
            countList.append(poppedCount+1)
        


        
s = '35'
print(solution(s))