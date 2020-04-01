
from IntCodeProgram import IntCodeProgram
import numpy as np

with open('day13.dat') as datafile:
    theprogram = datafile.readline()

def chunks(lst,n):
    """Yield successive n-sized chunks from lst"""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

game = IntCodeProgram(theprogram)

#observed = [1,2,3,6,5,4]
display = np.zeros( (24,44), dtype=np.int)

def implementAndDisplay(aGame, joystickPos):
    aGame.setInput([int(joystickPos)])
    aGame.process()
    observed = game.output

    blocks = 0
    score = 0
    ballloc = (0,0)
    paddleloc = (0,0)
    for atile in list(chunks(observed,3)):
        tiletype = int(atile[2])
        loc = (int(atile[1]), int(atile[0]))
        if tiletype == 2:
            blocks += 1
        if tiletype == 4:
            ballloc = loc
        if tiletype == 3:
            paddleloc = loc

        # more elegant would be to check for size

        if int(atile[0])==-1:
            score = int(atile[2])
        else:
            display[loc[0], loc[1]] = tiletype

    with np.printoptions(threshold=np.inf):
        print('\n'.join(''.join(str(cell) for cell in row) for row in display))

    print(f"Number of blocks: {blocks}   Score: {score}")
    return score, ballloc, paddleloc



print("PART 1")
implementAndDisplay(game,0)

print("PART 2")

game.reset()
game.memory[0] = 2

ballloc = (0,0)
paddleloc = (0,0)
while True:
    if ballloc[1] > paddleloc[1]:
        defpos = '1'
    elif ballloc[1] < paddleloc[1]:
        defpos = '-1'
    else:
        defpos = '0'
            
    joypos = input('Joystick?  -1=left, 0=hold, 1=right, def={}: '.format(defpos))
    if (joypos == ''):
        joypos = defpos

    (score, ballloc, paddleloc) = implementAndDisplay(game,joypos)
    print(f'game status={game.status}')
    print(f'Ball loc={ballloc},  paddle loc={paddleloc}')

