#import re
#import numpy
#import copy
#from IntCodeProgram import IntCodeProgram
import math
from blist import blist

with open('day10.dat') as datafile:
    asteroidmap = [x.strip() for x in datafile.readlines()]

test0 = """.#..#
.....
#####
....#
...##"""   # best at 3,4 with 8

test1 = """......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####"""  # best at 5,8 with 33 visible

#asteroidmap = [x.strip() for x in test1.splitlines()]

asteroids = {}
height = len(asteroidmap)
width = len(asteroidmap[0])

# collect asteroids
for iy, row in enumerate(asteroidmap):
    for ix, cell in enumerate(row):
        if cell == '#':
            asteroids[(ix,iy)] = 0

def isAsteroidVisible(aRoid, baseRoid):
    isx = 0
    isy = 1
    rise = aRoid[isy] - baseRoid[isy]
    run  = aRoid[isx] - baseRoid[isx]
    if run == 0:
        # flip axes so that we can look straight up and down too
        isx = 1
        isy = 0
        rise = aRoid[isy] - baseRoid[isy]
        run  = aRoid[isx] - baseRoid[isx]
    rundir = int(run / abs(run)) # 1=check>base, -1=check<base
    iblocks = 0
    for ixinc in range(1*rundir,run,rundir):
        yloc = rise/run*(ixinc) + baseRoid[isy]
        remainder = yloc - int(yloc)
        if (abs(remainder) < 1e-5):
            blockloc = (baseRoid[0] + ixinc,
                        int(yloc))
            if isx == 1:
                blockloc = (int(yloc),baseRoid[isx] + ixinc)
            if blockloc in asteroids:
                iblocks += 1
#                        print(f" blocked by {blockloc}")
                break
    if iblocks == 0:
        return True
    return False


# for each asteroid determine the count of visible
for base_asteroid, count in asteroids.items():
    # count the visible
    count = 0
#    print(f"ASTEROID {base_asteroid}:")
    for check_asteroid in asteroids.keys():
        if base_asteroid != check_asteroid:
            if isAsteroidVisible(check_asteroid,base_asteroid):
                count += 1
#                print(f"... visible!  count={count}")
    asteroids[base_asteroid] = count

maxcount = 0
maxcount_roid = None
for aasteroid,count in asteroids.items():
    if count > maxcount:
        maxcount = count
        maxcount_roid = aasteroid

print(f"Maxcount Asteroid at {maxcount_roid} has count={maxcount}")            

base_location = maxcount_roid
asteroids.pop(base_location)

minangle = math.atan2(0-height, 0-width) - math.atan2(0-height, 1-width)
maxdist = math.sqrt(height**2 + width**2)

def calcAngle(location):
    global base_location
    ydist = location[1] - base_location[1]
    xdist = location[0] - base_location[0]
    ang = math.atan2(ydist,xdist) + math.pi/2
    if ang < 0:
        ang += 2*math.pi
    # need a tiebreaker... furthest away should go first
    totdist = math.sqrt(ydist**2 + xdist**2)
    penalty = totdist / maxdist * abs(minangle)
    ang -= penalty
    return ang
    

remaining_roids = blist(sorted(asteroids.keys(), key=calcAngle))

count_destroyed = 0
last_destroyed = None
while count_destroyed < len(remaining_roids):
    for i,aRoid in enumerate(remaining_roids):
        if aRoid != None:
            if isAsteroidVisible(aRoid,base_location):
                # kill it
                last_destroyed = aRoid
                remaining_roids[i] = None
                count_destroyed += 1
                print(f"Destroyed {count_destroyed} at {last_destroyed}")


