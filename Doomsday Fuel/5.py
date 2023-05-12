from fractions import Fraction

def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def identityMatrix(n):
    final = [[0]*n for _ in range(n)]
    for i in range(n):
        final[i][i] = 1
    return final


def subtractMatrices(m1, m2):
    final = []
    for i in range(len(m1)):
        tmp = []
        m1Row = m1[i]
        m2Row = m2[i]
        for j in range(len(m1Row)):
            tmp.append(m1Row[j] - m2Row[j])
        final.append(tmp)
    return final


def matrixMultiplication(m1, m2):
    m1Row, _ = len(m1), len(m1[0])
    _, m2Column = len(m2), len(m2[0])
    final = [[0]*m2Column for _ in range(m1Row)]
    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                final[i][j] += m1[i][k] * m2[k][j]

    return final


def invertMatrix(matrix):
    n = len(matrix)
    identity = identityMatrix(n)
    
    for i in range(n):
        diagonal = matrix[i][i]
        for j in range(n):
            matrix[i][j] /= diagonal
            identity[i][j] /= diagonal
        
        for j in range(n):
            if i == j:
                continue
            factor = matrix[j][i]
            for k in range(n):
                matrix[j][k] -= factor * matrix[i][k]
                identity[j][k] -= factor * identity[i][k]
    
    return identity



def transitionMatrix(m):
    for idx, row in enumerate(m):
        sumIdxRow = sum(row)
        if sumIdxRow == 0:
            m[idx][idx] = 0
        else:
            for i in range(len(row)):
                m[idx][i] = Fraction(m[idx][i], sumIdxRow)
    return m



def qrMatrices(transitionedMatrix, transientStates, absorbingStates):
    q = []
    r = []
    for row in transientStates:
        qTmp = []
        rTmp = []
        for column in transientStates:
            qTmp.append(transitionedMatrix[row][column])
        for column in absorbingStates:
            rTmp.append(transitionedMatrix[row][column])
        q.append(qTmp)
        r.append(rTmp)
    return q, r
        


def lcm(array):
    result = array[0]
    for element in array[1:]:
      result = result * element // gcd(result, element)
    return result


def solution(m):
    transientStates = []
    absorbingStates = []
    for i in range(len(m)):
        row = m[i]
        if sum(row) == 0:
            absorbingStates.append(i) 
        else:
            transientStates.append(i)
    if len(absorbingStates)==1:
        return [1, 1]
    m = transitionMatrix(m)

    q, r = qrMatrices(m, transientStates, absorbingStates)
    identity = identityMatrix(len(q))
    diff = subtractMatrices(identity, q)
    inverse = invertMatrix(diff)
    m2 = matrixMultiplication(inverse, r)

    denominatorList = []
    numeratorList = []
    for element in m2[0]:
        denominatorList.append(element.denominator)
        numeratorList.append(element.numerator)

    denominator = lcm(denominatorList)
    result = []
    for idx, numerator in enumerate(numeratorList):
        result.append(numerator * denominator//denominatorList[idx])
    result.append(denominator)
    return result




m1 = [[0, 2, 1, 0, 0], [0, 0, 0, 3, 4], [0, 0, 0, 0, 0], [0, 0, 0, 0,0], [0, 0, 0, 0, 0]]
m2 = [[0, 1, 0, 0, 0, 1], [4, 0, 0, 3, 2, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]

o1 = [7, 6, 8, 21]
o2 = [0, 3, 2, 9, 14]

print(solution(m1)==o1)
print(solution(m2)==o2)