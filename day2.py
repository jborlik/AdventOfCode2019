import copy

with open('day2.dat') as datafile:
    alldata = [int(x) for x in datafile.readline().split(sep=',')]

def runToHalting(theMemory):

    iloc = 0
    ishalted = False

    while not ishalted:
        iop = theMemory[iloc]
        if (iloc+3) < len(theMemory):
            iloc1 = theMemory[iloc + 1]
            iloc2 = theMemory[iloc + 2]
            ilocput = theMemory[iloc + 3]
            
        if (iop == 1):
            val = theMemory[iloc1] + theMemory[iloc2]
            theMemory[ilocput] = val
        elif (iop == 2):
            val = theMemory[iloc1] * theMemory[iloc2]
            theMemory[ilocput] = val
        else:
            #print("Halting with instruction ", iop)
            ishalted = True
        iloc += 4

def runSafeWithNounVerb(noun, verb, theMemory):
    myMemory = copy.deepcopy(theMemory)
    myMemory[1] = noun
    myMemory[2] = verb
    runToHalting(myMemory)
    return myMemory[0]

#alldata = [1,9,10,3,2,3,11,0,99,30,40,50]
#alldata = [1,0,0,0,99]
#alldata = [1,1,1,4,99,5,6,0,99]


part1result = runSafeWithNounVerb(12,2, alldata)
print("Part 1: ", part1result)

for anoun in range(0,len(alldata)-1):
    for averb in range(0,len(alldata)-1):
        aresult = runSafeWithNounVerb(anoun,averb, alldata)
        if aresult == 19690720:
            print("GOT IT PART2: 100*{} + {}={}".format(anoun, averb, 100*anoun + averb))
            exit()


