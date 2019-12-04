import numpy as np

with open('day3.dat') as datafile:
    path = [x.split(',') for x in datafile.readlines()]

teststr_0 = """R8,U5,L5,D3
U7,R6,D4,L4"""
teststr_1 = """R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83"""   #ans=159
teststr_2 = """R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"""   #ans=135
testpath0 = [x.split(',') for x in teststr_0.splitlines()]
testpath1 = [x.split(',') for x in teststr_1.splitlines()]
testpath2 = [x.split(',') for x in teststr_2.splitlines()]

MAXSIZE = 50000
ORIGIN = int(MAXSIZE/2)
workingarr = np.zeros((MAXSIZE,MAXSIZE),dtype=int)

thepath = path

def processInstructions(world, instructions, wireid):
    locx = 0
    locy = 0
    for aIns in instructions:
        (locx,locy) = processInstruction(world, aIns, locx, locy, wireid)

def processInstruction(world, theInstruction, locx, locy, wireid):
    dirr  = theInstruction[0]
    dist = int(theInstruction[1:])
    walkarr = {"U": (0,-1), "D": (0,1), "R": (1,0), "L": (-1,0) }
    for i in range(0,dist):
        locx += walkarr[dirr][0]
        locy += walkarr[dirr][1]
        #print('walking {}{}:  step {}, at x={} y={} currval={}'.format(dirr,dist,i,locx,locy, world[locx+ORIGIN,locy+ORIGIN]))
        world[locx+ORIGIN,locy+ORIGIN] = world[locx+ORIGIN,locy+ORIGIN] | wireid
    return (locx,locy)

processInstructions(workingarr, thepath[0], 1)
print(workingarr)
processInstructions(workingarr, thepath[1], 2)
print(workingarr)

crosses = np.where(workingarr == 3)
mindist = 100000
mincross = ()
for across in zip(crosses[0],crosses[1]):
    thedist = abs(across[0]-ORIGIN) + abs(across[1]-ORIGIN)
    if thedist < mindist:
        mindist = thedist
        mincross = across
print("Min distance crossing at {} with distance={}".format(mincross, mindist))




#if __name__ == "__main__":
#    runPart1()
