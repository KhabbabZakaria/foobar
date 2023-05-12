'''def solution(h, q):
    levelsFinal = binaryTree(h)
    result = []
    for v in q:
        for idx, val in enumerate(levelsFinal):
            if v in val and idx==0:
                found = -1
                break
            elif v in val:
                found = [idx, val.index(v)]
                break
            else:
                found = -1
        if found==-1:
            result.append(-1)
        else:
            vertical=found[0]-1
            horizontal=found[1]//2
            result.append(levelsFinal[vertical][horizontal])
    return result'''

#parent = n.... children 2n+1 2n+2
# parent = (n-1)//2  .... children n
# 15 7 14 3 6 10 13 1 2 4 5 8 9 11 12

def solution(h, q):
    levels = binaryTree(h)
    result = []
    for v in q:
        try:
            idx = levels.index(v)
            if idx==0:
                result.append(-1)
            else:
                result.append(levels[(idx-1)//2])
        except:
            result.append(-1)
    return result

        

def binaryTree(h):
    if h==1:
        return 1
    headVal = 0
    for i in range(h):
        headVal+=2**i
    tree = list(range(1, headVal+1))
    popped = tree.pop() 
    levels = [popped] 
    graph = [tree] 
    while len(graph):
        tree = graph.pop(0)
        mid = len(tree)//2
        left = tree[:mid]
        right = tree[mid:]
        poppedL = left.pop()
        poppedR = right.pop()
        levels.append(poppedL)
        levels.append(poppedR)
        if len(left)>0 and len(right)>0:
            graph.append(left)
            graph.append(right)
    return levels

h1,q1=3, [7, 3, 5, 1]
h2,q2=5, [19, 14, 28]

#print(solution(h1,q1))

o1=[-1,7,6,3]
o2=[21,15,29]
print(solution(h1,q1)==o1)
print(solution(h2,q2)==o2)

