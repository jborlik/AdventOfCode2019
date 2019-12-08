import itertools
from IntCodeProgram import IntCodeProgram

with open('day7.dat') as datafile:
    alldata = datafile.readline()

#alldata = '3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0'  # 43210
#alldata = '3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0'   # 54321

phases = [0,1,2,3,4]

amps = [IntCodeProgram(alldata) for x in range(0,5)]

maxthrust = 0
maxthrust_phasechoice = []
for phasechoice in itertools.permutations(phases,5):
    lastinput = 0
    for i,amp in enumerate(amps):
        amp.reset()
        amp.setInput([phasechoice[i], lastinput])
        amp.process()
        lastinput = amp.output[0]
    if lastinput > maxthrust:
        maxthrust = lastinput
        maxthrust_phasechoice = phasechoice

    
print(f"maxthrust={maxthrust} with phasechoice={maxthrust_phasechoice}")

