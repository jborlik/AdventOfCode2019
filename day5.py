from IntCodeProgram import IntCodeProgram, OpCode



print(OpCode(1002))
print(OpCode(2))

test1 = IntCodeProgram('3,0,4,0,99')
test1.setInput([10])
test1.process()
print(f"Test1 input={test1.input} output={test1.output}")
print(f"memory={test1.memory}")

test2 = IntCodeProgram('1002,4,3,4,33')
test2.process()
print(f'Test2 memory={test2.memory}')


with open('day5.dat') as datafile:
    alldata = datafile.readline()


part1 = IntCodeProgram(alldata)
part1.setInput([1])
part1.process()
print(f'Part1 output={part1.output}')

test3 = IntCodeProgram('3,9,8,9,10,9,4,9,99,-1,8')   # consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not)
test3.setInput([8])
test3.process()
print(f'Test3 output={test3.output}')  # if input=8, then 1

part2 = IntCodeProgram(alldata)
part2.setInput([5])
part2.process()
print(f'Part2 output={part2.output}')

