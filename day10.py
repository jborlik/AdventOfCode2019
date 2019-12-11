#import re
#import numpy
#import copy
#from IntCodeProgram import IntCodeProgram


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

# for each asteroid determine the count of visible
for base_asteroid, count in asteroids.items():
    # count the visible
    count = 0
#    print(f"ASTEROID {base_asteroid}:")
    for check_asteroid in asteroids.keys():
        if base_asteroid != check_asteroid:
#            print(f"  checking asteroid {check_asteroid}", end='')
            isx = 0
            isy = 1
            rise = check_asteroid[isy] - base_asteroid[isy]
            run  = check_asteroid[isx] - base_asteroid[isx]
            if run == 0:
                # flip axes so that we can look straight up and down too
                isx = 1
                isy = 0
                rise = check_asteroid[isy] - base_asteroid[isy]
                run  = check_asteroid[isx] - base_asteroid[isx]
            rundir = int(run / abs(run)) # 1=check>base, -1=check<base
            iblocks = 0
            for ixinc in range(1*rundir,run,rundir):
                yloc = rise/run*(ixinc) + base_asteroid[isy]
                remainder = yloc - int(yloc)
                if (abs(remainder) < 1e-5):
                    blockloc = (base_asteroid[0] + ixinc,
                                int(yloc))
                    if isx == 1:
                        blockloc = (int(yloc),base_asteroid[isx] + ixinc)
                    if blockloc in asteroids:
                        iblocks += 1
#                        print(f" blocked by {blockloc}")
                        break
            if iblocks == 0:
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


    


