
from IntCodeProgram import IntCodeProgram

with open('day13.dat') as datafile:
    theprogram = datafile.readline()

def chunks(lst,n):
    """Yield successive n-sized chunks from lst"""
    for i in range(0, len(lst), n):
        yield lst[i:i+n]

game = IntCodeProgram(theprogram)

game.process()
observed = game.output

#observed = [1,2,3,6,5,4]

display = {}
blocks = 0
for atile in list(chunks(observed,3)):
    tiletype = int(atile[2])
    if tiletype == 2:
        blocks += 1
    display[(int(atile[0]), int(atile[1]))] = tiletype

print("Number of elements: ", len(display))
print(f"Number of blocks: {blocks}")




