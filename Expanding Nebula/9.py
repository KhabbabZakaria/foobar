
def return_conjugations(a,b,c,d):
    return (a&~b&~c&~d) | (~a&b&~c&~d) | (~a&~b&c&~d) | (~a&~b&~c&d)

def generate_comb(val1,val2,bitlen):
    a = val1 & ~(1<<bitlen) #left shift
    b = val2 & ~(1<<bitlen)
    c = val1 >> 1 #right shift
    d = val2 >> 1
    return return_conjugations(a,b,c,d)

def mapping_helper(generation, i, j, keylist, mapping):
    if (generation, i) in keylist:
        val = mapping[(generation, i)]
        val.append(j)
        return val
    return [j]

def mapping_fn(len, nums):
    mapping = {}
    nums = set(nums)
    for i in range(1<<(len+1)):
        for j in range(1<<(len+1)):
            generation = generate_comb(i,j,len)
            if generation in nums:
                keylist = list(mapping.keys())
                mapping[(generation,i)] = mapping_helper(generation, i, j, keylist, mapping)                

    return mapping



def solution(matrix):
    matrix = list(zip(*matrix)) # transpose

    # turn map into numbers
    nums = []
    for i in range(len(matrix)):
        tmp = []
        for j in range(len(matrix[i])):
            if matrix[i][j]:
                tmp.append(1<<j)
            else:
                tmp.append(0)
        nums.append(sum(tmp))

    mapping = mapping_fn(len(matrix[0]), nums)

    preimage = {i: 1 for i in range(1<<(len(matrix[0])+1))}
    for row in nums:
        next_row = {}
        for c1 in preimage:
            keylist = list(mapping.keys())
            if (row, c1) not in keylist:
                mapping[(row, c1)] = []
            for c2 in mapping[(row, c1)]:
                keylist = list(next_row.keys())
                if c2 in keylist:
                    next_row[c2] += preimage[c1]
                else:
                    next_row[c2] = preimage[c1]
        preimage = next_row
    ret = sum(preimage.values())

    return ret


