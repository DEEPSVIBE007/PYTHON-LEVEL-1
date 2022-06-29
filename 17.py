def swapList(newList):
    size = len(newList)
     
    temp = newList[0]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     
    return newList
     
newList = [32, 38, 5, 68, 35]
 
print(swapList(newList))
