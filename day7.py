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

    
print(f"Part 1: maxthrust={maxthrust} with phasechoice={maxthrust_phasechoice}")

# Part 2!

maxthrust = 0
maxthrust_phasechoice = []

# test, max thrust=139629729 (from phase setting sequence 9,8,7,6,5)
#alldata = '3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5'

amps = [IntCodeProgram(alldata) for x in range(0,5)]
phases = [5,6,7,8,9]

def processAmp(amp, nextAmp):
    amp.process()
    nextAmp.input.extend(amp.output)
    if amp.status != 'Halted':
        amp.output = []

for phasechoice in itertools.permutations(phases,5):
    for i,amp in enumerate(amps):
        amp.reset()
        amp.setInput([phasechoice[i]])
    amps[0].input.append(0)

    # iterate 
    alldone = False
    while not alldone:
#        print(f'Amp 0: input={amps[0].input}')
        processAmp(amps[0], amps[1])
#        print(f'Amp 1: input={amps[1].input}')
        processAmp(amps[1], amps[2])
#        print(f'Amp 2: input={amps[2].input}')
        processAmp(amps[2], amps[3])
#        print(f'Amp 3: input={amps[3].input}')
        processAmp(amps[3], amps[4])
#        print(f'Amp 4: input={amps[4].input}')
        processAmp(amps[4], amps[0])
        if amps[4].status == 'Halted':
            alldone = True


    if amps[4].output[0] > maxthrust:
        maxthrust = amps[4].output[0]
        maxthrust_phasechoice = phasechoice

print(f"Part 2: maxthrust={maxthrust} with phasechoice={maxthrust_phasechoice}")
