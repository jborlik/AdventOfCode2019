#import re
import numpy as np
#import copy
#from IntCodeProgram import IntCodeProgram

moons = [
    [[-10,-10,-13],[0,0,0]],
    [[5,5,-9],[0,0,0]],
    [[3,8,-16],[0,0,0]],
    [[1,3,-3],[0,0,0]]
]

#moons = [   #example.  energy =179 after 10
#    [ [-1,0,2], [0,0,0]],
#    [ [2,-10,-7], [0,0,0]],
#    [ [4,-8,8], [0,0,0]],
#    [ [3,5,-1], [0,0,0]]
#]
POSITION = 0
VELOCITY = 1

STEPS = 1000

def updateVelocity():
    for im,moon in enumerate(moons):
        # update moon velocity by comparing with the others
        for ix,othermoon in enumerate(moons):
            if im != ix:
                for axis in range(0,3):
                    moon[VELOCITY][axis] += np.sign(othermoon[POSITION][axis] - moon[POSITION][axis])

def updatePosition():
    for moon in moons:
        for axis in range(0,3):
            moon[POSITION][axis] += moon[VELOCITY][axis]

def sumEnergy():
    totalenergy = 0
    for moon in moons:
        thisenergy = 1
        for itype in range(0,2):
            typeenergy = 0
            for axis in range(0,3):
                typeenergy += abs(moon[itype][axis])
            thisenergy *= typeenergy
        totalenergy += thisenergy
    return totalenergy



for i in range(0,STEPS):
#    print(f'After {i} steps:')
#    for moon in moons:
#        print(f'pos={moon[0]} vel={moon[1]}')
    updateVelocity()
    updatePosition()

print(f'After {STEPS} steps:')
for moon in moons:
    print(f'pos={moon[0]} vel={moon[1]}')
print("Total energy=",sumEnergy())
