
width, height = 25, 6
#width, height = 3, 2


with open('day8.dat') as datafile:
    alldata = datafile.readline().strip()

#alldata = '123456789012'

chunk_size = width*height
chunks = int(len(alldata) / chunk_size)
layerstrings = [ alldata[i:i+chunk_size] for i in range(0, len(alldata), chunk_size) ]
# now I have layers by string
#print(layerstrings)

data = []
for alayer in layerstrings:
#    rowstrings = [ alayer[i:i+width] for i in range(0, height*width, width) ]
#    rowints = [ list(map(int, list(x))) for x in rowstrings]
    rowints = [ int(x) for x in alayer]
    data.append(rowints)

print(data)
# find layer with max zeros
leastlayer = -1
leastvalues = [100,0,0]
for ilayer, alayer in enumerate(data):
    counts = [ alayer.count(0), alayer.count(1), alayer.count(2)]
    print(f'on layer {ilayer}, counts={counts}')
    if counts[0] < leastvalues[0]:
        leastvalues = counts
        leastlayer = ilayer

print(f'Part 1: on layer {leastlayer}, 1s*2s={leastvalues[1]*leastvalues[2]}')

# resolve picture
thepic = [2 for x in range(0,width*height)]
for i in range(0,width*height):
    for alayer in data:
        if alayer[i] != 2:
            thepic[i] = alayer[i]
            break

# display
#    rowstrings = [ alayer[i:i+width] for i in range(0, height*width, width) ]
for irow in range(0,height):
    print(''.join(str(x) for x in thepic[irow*width:(irow+1)*width]))
