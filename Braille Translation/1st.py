def solution(s):
    code_table = {
    'a': '100000',
    'b': '110000',
    'c': '100100',
    'd': '100110',
    'e': '100010',
    'f': '110100',
    'g': '110110',
    'h': '110010',
    'i': '010100',
    'j': '010110',
    'k': '101000',
    'l': '111000',
    'm': '101100',
    'n': '101110',
    'o': '101010',
    'p': '111100',
    'q': '111110',
    'r': '111010',
    's': '011100',
    't': '011110',
    'u': '101001',
    'v': '111001',
    'w': '010111',
    'x': '101101',
    'y': '101111',
    'z': '101011',
    '#': '001111',
    '1': '100000',
    '2': '110000',
    '3': '100100',
    '4': '100110',
    '5': '100010',
    '6': '110100',
    '7': '110110',
    '8': '110010',
    '9': '010100',
    '0': '010110',
    ' ': '000000'}
    keyList = list(code_table.keys())
    listIdxAllCaps = []
    sList = s.split(' ')
    for _, val in enumerate(sList):
        allCaps = True
        for v in val:
            if v in keyList:
                allCaps = False
                break
        if allCaps:
            listIdxAllCaps.append(s.index(val))
    result = ''
    for idx, val in enumerate(s):
        try:
            result += code_table[val]
        except:
            if idx in listIdxAllCaps:
                result += '000001000001' + code_table[val.lower()]
            else:
                result += '000001' + code_table[val.lower()]
    return result






s1 = 'code'
s2 = 'Braille'
s3 = 'The quick brown fox jumps over the lazy dog'

o1 = '100100101010100110100010'
o2 = '000001110000111010100000010100111000111000100010'
o3 = '000001011110110010100010000000111110101001010100100100101000000000110000111010101010010111101110000000110100101010101101000000010110101001101100111100011100000000101010111001100010111010000000011110110010100010000000111000100000101011101111000000100110101010110110'


print(solution(s2))
print(solution(s1)==o1)
print(solution(s2)==o2)
print(solution(s3)==o3)



