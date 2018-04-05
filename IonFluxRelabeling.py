import math
def answer(h,q):
    height = h
    fluxConverters = q
    print(len(q))
    parentList = []*len(q)
    maxValue = 2**height -1
    currentValue = maxValue
    traverseRightOccurred = False

    for i in range(len(q)):
        currentValue = maxValue
        traverseRightOccurred = False
        for j in range(h):
            if(traverseRightOccurred):
                if(fluxConverters[i] == maxValue): # case: root
                    parentList.append(-1)
                    break
                elif(fluxConverters[i] == currentValue - 2**(height - (j+1))): # found value traversing left
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] == currentValue-1): # found value traversing right
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] < currentValue - 2**(height - (j+1))): # traversing left
                    currentValue = currentValue - 2**(height - (j+1))
                elif(fluxConverters[i] < currentValue-1): # traversing right
                    currentValue = currentValue-1
            else:               # traverse right has not occurred
                if(fluxConverters[i] == maxValue): # case: root
                    parentList.append(-1)
                    break
                elif(fluxConverters[i] == math.floor(currentValue/2)): # found value traversing left
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] == currentValue-1): # found value traversing right
                    parentList.append(currentValue)
                    break
                elif(fluxConverters[i] < math.floor(currentValue/2)): # traversing left
                    currentValue = math.floor(currentValue/2)
                elif(fluxConverters[i] < currentValue-1): # traversing right
                    currentValue = currentValue-1
                    traverseRightOccurred = True
    return parentList

h = 3
q = [7,3,5,1] 
print(answer(h,q))
# answer = [-1,7,6,3]

h = 3
q = [1,4,7]
print(answer(h,q))
# answer = [3,6,-1]

h = 5
q = [1,6, 10, 12, 15, 22, 30, 18, 20, 26, 29]
print(answer(h,q))
# answer = [3,7,14,13,31,30,31,22,21,28,30]
