treesRead = open("input3.txt")
trees = (treesRead.read().split('\n'))

posstart = 0 
positionCalc = len(trees[0]) 
numOfTrees = 0 

for treerow in trees: 
    if treerow[posstart] == "#":
        numOfTrees += 1 
    posstart = posstart + 3
    if posstart >= positionCalc: 
        posstart = posstart%positionCalc

print(numOfTrees)

#Teil 2 

def treeCount(x, y):
    pos1 = 0 
    treeNum = 0 
    count = 0 
    for treerow in trees: 
        #count = count + 1
        if count%y != 0:  

           # print("oh no", count, y, count%y)
            count = count + 1
            continue
        else:
            if treerow[pos1] == "#":
                treeNum = treeNum + 1
              #  print(count, pos1, treeNum)
            count = count + 1
        pos1 = pos1 + x
        if pos1 >= positionCalc: 
            pos1 = pos1%positionCalc
        
    return treeNum 

print(treeCount(1,1))
print(treeCount(3,1))
print(treeCount(5,1))
print(treeCount(7,1))
print(treeCount(1,2))

solution = treeCount(3,1) * treeCount(1,2) * treeCount(1,1) * treeCount(5,1) * treeCount(7,1)
print(solution)