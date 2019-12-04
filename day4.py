

#with open('day4.dat') as datafile:
#    alldata = [x.split(',') for x in datafile.readlines()]

puzzle_min = 245318
puzzle_max = 765747


def checkNumber(aNum,usesPartTwoRule):
    # rule 1
    if aNum < 100000:
        return False
    if aNum > 999999:
        return False
    # rule 2
    #if aNum < puzzle_min:
    #    return False
    #if aNum > puzzle_max:
    #    return False
    # rule 3/4
    sNum = str(aNum)

    countDoubles = 0
    for istart in range(0,5):
        # rule 4
        #print("{} < {}? (istart={}).  {}".format(sNum[istart], sNum[istart+1], istart, (sNum[istart] > sNum[istart+1])))
        if sNum[istart] > sNum[istart+1]:
            return False
        if sNum[istart] == sNum[istart+1]:
            if usesPartTwoRule:
                # check behind / ahead for extra
                ispartofagroup = False
                if istart > 0:
                    if sNum[istart-1] == sNum[istart]:
                        ispartofagroup = True
                if istart < 4:
                    if sNum[istart+2] == sNum[istart]:
                        ispartofagroup = True
                if not ispartofagroup:
                    countDoubles += 1
                
            else:
                countDoubles += 1

    if countDoubles == 0:
        return False
    return True

print("111111? part 1: ", checkNumber(111111,False))
print("223450? part 1:  ", checkNumber(223450,False))
print("123789? part 1:  ", checkNumber(123789,False))
print("765559? part 1:  ", checkNumber(765559,False))
print("112233? part 2: yes: ", checkNumber(112233,True))
print("223450? part 2: no: ", checkNumber(223450,True))
print("111122? part 2: yes ", checkNumber(111122,True))

totalcount = 0
for aNum in range(puzzle_min,puzzle_max+1):
    if checkNumber(aNum,False):
        #print("found {}: {}".format(totalcount, aNum))
        totalcount += 1

print("Part 1:  Total count = ", totalcount)

totalcount = 0
for aNum in range(puzzle_min,puzzle_max+1):
    if checkNumber(aNum,True):
        #print("found {}: {}".format(totalcount, aNum))
        totalcount += 1

print("Part 2:  Total count = ", totalcount)

#if __name__ == "__main__":
#    runPart1()
