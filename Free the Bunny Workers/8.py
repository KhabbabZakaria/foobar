import itertools

def generateBunnyCombinations(num_buns, num_required):
    r = num_buns - num_required + 1
    iterator = range(num_buns)
    combinations = list(itertools.combinations(iterator, r))
    return combinations


def solution(num_buns, num_required):
    bunniesHavingSameKeysList = generateBunnyCombinations(num_buns, num_required)
    bunniesList = []
    for idx, bunniesHavingSameKeys in enumerate(bunniesHavingSameKeysList):
        #check if the list exists
        for bunny in bunniesHavingSameKeys:
            try:
                bunniesList[bunny].append(idx)
            except:
                tmp = [idx]
                bunniesList.append(tmp)
    return bunniesList