def Main():
    f = open("Day-2-Passwords.txt", "r")
    p1Counter = 0#Result for part 1
    p2Counter = 0#Result for part 2
    for x in f:#
        currentPolicy = x.split()#Split the string in to different parts
        min, max = int(currentPolicy[0].split('-')[0]), int(currentPolicy[0].split('-')[1]) #find the min/max vaules
        Letter = currentPolicy[1][0]#Find the letter to search for
        pw = currentPolicy[2] #Find the password
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
    if instanceCounter<=max and instanceCounter>=min:
        return 1
    else:
        return 0

#Checks validation for part 2
def PartTwo(pos1,pos2,Letter,pw):
        if (pw[pos1-1]==Letter and pw[pos2-1]!=Letter) or (pw[pos1-1]!=Letter and pw[pos2-1]==Letter):
            return 1
        else:
            return 0


print(Main())
