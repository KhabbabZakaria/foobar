def baseto10(num, base):
    result = 0
    for i in range(len(num)):
        result += int(num[-i-1]) * base**i
    return result

def basefrom10(num, base):
    result = ''
    while num > 0:
        remainder = num % base
        num //= base
        result += str(remainder)

    result = result[::-1]
    return result

def minus(k, b):
    kList = []
    for i in k:
        kList.append(i)
    kList.sort()
    kMin = ''.join(kList)
    kMax = ''.join(kList[::-1])
    kMin = baseto10(kMin, b)
    kMax = baseto10(kMax, b)
    minusVal = kMax - kMin
    minusVal = str(basefrom10(minusVal, b))
    diffInLength = len(k) - len(minusVal)
    final = ''
    for i in range(diffInLength):
        final+='0'
    final+=minusVal
    return final


def solution(n, b):
    already = []
    while True:
        final = minus(n,b)
        if final not in already:
            already.append(final)
            n = final
        else:
            idx = already.index(final)
            break
    return len(already) - idx




print(solution('210022', 3)==3)

print(solution('1211', 10)==1)