#BTW I know that opening the file over and over again is bad, and I could just loop it 5 times with one open
def Main(initialX,isSlope5):
    #Each line before repeating is 32 chars
    f = open("Day-3-map.txt", "r")
    currentX=initialX
    xIncrement=initialX
    treeCounter=0
    for iteration ,x in enumerate(f):
        #Ignore the first line because it's never a tree
        if iteration==0: #or iteration%2!=0: #Uncomment for part2 5th slope
            continue
        if isSlope5:
            if iteration%2!=0:
                continue
        if currentX>(len(x)-2): #Have to do len(x)-2 because of the \n character which is not shown
            currentX=currentX-(len(x)-1)
        treeCounter+=int(x[currentX]=="#")
        currentX += xIncrement
    f.close()
    return treeCounter

part2Answer=0
part1Answer=0

part2Answer+=Main(1,False)
part1Answer=Main(3,False)
print("Part1: ",part1Answer)
part2Answer=part2Answer*part1Answer
part2Answer=part2Answer*Main(5,False)
part2Answer=part2Answer*Main(7,False)
part2Answer=part2Answer*Main(1,True)
print("Part2: ",part2Answer)
