def solution(entrances, exits, path):
    intermediates = []
    for i in range(len(path)):
        if i not in entrances and i not in exits:
            intermediates.append(i)

    comingFromList = [ [] for _ in range(len(path)) ]
    for room, nextRooms in enumerate(path):
        for nextRoom, val  in enumerate(nextRooms):
            if val!=0 and room not in exits:
                comingFromList[nextRoom].append(room)

    maxPossibleInRoom = []
    for element in path:
        maxPossibleInRoom.append(sum(element))

    bunnyCount = 0
    prevCount = {}
    for intermediate in intermediates:
        comingFrom = comingFromList[intermediate]
        tmp = 0
        for prev in comingFrom:
            if prev in entrances:
                tmp += path[prev][intermediate]
            else:
                bunnyCount -= prevCount[prev]
                tmp = min(prevCount[prev], maxPossibleInRoom[intermediate])
        bunnyCount += min(tmp, maxPossibleInRoom[intermediate])
        prevCount[intermediate] = min(tmp, maxPossibleInRoom[intermediate])
    
    return bunnyCount




entrances = [0, 1]
exits = [4, 5]
path = [
  #0  1  2  3  4  5#
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies ============== 10
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies ============== 7
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room ==== 8
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room ==== 12
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]



#print(solution(entrances, exits, path))



entrances = [0]
exits = [3]
path =[[0, 7, 0, 0], 
       [0, 0, 6, 0], 
       [0, 0, 0, 8], 
       [9, 0, 0, 0]]

print(solution(entrances, exits, path))
