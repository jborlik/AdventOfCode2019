import re
from IntCodeProgram import IntCodeProgram


with open('day9.dat') as datafile:
    alldata = datafile.readline()

part1 = IntCodeProgram(alldata)
part1.setInput([1])
part1.process()
print(f'Part1 output={part1.output}')
print(f'status={part1.status}')

part2 = IntCodeProgram(alldata)
part2.setInput([2])
part2.process()
print(f'Part2 output={part2.output}')