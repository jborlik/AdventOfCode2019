
with open('day1.dat') as datafile:
    alldata = [int(x.strip()) for x in datafile.readlines()]

testdata = [100756]

#alldata = testdata

def fuelreq(weight):
    return max( int(weight / 3)-2, 0)


fuelsum = 0

for aNum in alldata:
    fuelsum += fuelreq(aNum)
print("Part1 Sum=",fuelsum)

fuelsum = 0

for aNum in alldata:
    weight = aNum
    while (weight > 0):
        addfuel = fuelreq(weight)
        fuelsum += addfuel
        weight = addfuel

print("Part2 Sum=",fuelsum)




