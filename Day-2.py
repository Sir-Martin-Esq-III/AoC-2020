def Main():
    f = open("Day-2-Passwords.txt", "r")
    p1Counter = p2Counter = 0
    for x in f:#
        currentPolicy = x.split()#Split the string in to different parts
        min, max = int(currentPolicy[0].split('-')[0]), int(currentPolicy[0].split('-')[1]) #find the min/max vaules
        Letter,pw = currentPolicy[1][0],currentPolicy[2]#Get the letter and pw
        p1Counter+=PartOne(min,max,Letter,pw)
        p2Counter+=PartTwo(min,max,Letter,pw)
    f.close()
    return(p1Counter,p2Counter)

#Checks validation for part 1
def PartOne(min,max,Letter,pw):
    instanceCounter=0
    for cururentLetter in pw:
        if cururentLetter==Letter:
            instanceCounter+=1
    return int(min<=instanceCounter<=max)

#Checks validation for part 2
def PartTwo(pos1,pos2,Letter,pw):
    return int((pw[pos1-1]==Letter) ^ (pw[pos2-1]==Letter))

print(Main())
