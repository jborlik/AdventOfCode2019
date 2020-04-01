#  The IntCodeProgram, as described by days 2 and 5

# Day 5 has a number of tests for this

class OpCode:
    def __init__(self, intcode):
        self.intcode = intcode
        stcode = f'{intcode:05}'
        self.code = int(stcode[-2:])
        self.modes = stcode[len(stcode)-3::-1]
    def __str__(self):
        return f'code={self.code} modes={self.modes}'

class IntCodeProgram:
    def __init__(self, programline):
        self.initial_prog = programline
        self.input = []
        self.reset()

    def reset(self):
        self.memory = [int(x) for x in self.initial_prog.split(sep=',')]
        self.instruction_pointer = 0
        self.input_pointer = 0
        self.output = []
        self.status = 'Initialized'
        self.relative_base = 0
        # leaving self.input alone

    def setInput(self, theinput):
        self.input = theinput
        self.input_pointer = 0

    def process(self):
        iscontinuing = True
        self.status = 'Running'
        while iscontinuing:
            iscontinuing = self.processNextInstructionAndContinue()

    def expandMemoryIfNeeded(self,parameterNeeded):
        if parameterNeeded >= len(self.memory):
            self.memory.extend([0 for x in range(parameterNeeded-len(self.memory)+1)])

    def resolveValue(self, parameter, mode):
        if mode == '0':
            # position mode
            self.expandMemoryIfNeeded(parameter)
            return self.memory[parameter]
        if mode == '1':
            # immediate mode
            return parameter
        if mode == '2':
            # relative mode
            self.expandMemoryIfNeeded(parameter + self.relative_base)
            return self.memory[parameter + self.relative_base]
        return 0

    def storeValue(self, parameter, mode, value):
        if mode == '0':
            # position mode
            locput = self.memory[parameter]
            self.expandMemoryIfNeeded(locput)
            self.memory[locput] = value
        if mode == '1':
            # immediate mode
            print('huh?  immediate mode not value for storing')
        if mode == '2':
            # relative mode
            locput = self.memory[parameter] + self.relative_base
            self.expandMemoryIfNeeded(locput)
            self.memory[locput] = value

    def processNextInstructionAndContinue(self):
        thisOp = OpCode(self.memory[self.instruction_pointer])
        pointer_increment = 0
        willcontinue = True

        if thisOp.code == 1:
            #  Addition:  1,a,b,loc
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            retval = val0 + val1
            self.storeValue(self.instruction_pointer + 3,thisOp.modes[2], retval)
            pointer_increment = 4
        elif thisOp.code == 2:
            #  Multiplication:  2,a,b,loc
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            retval = val0 * val1
            self.storeValue(self.instruction_pointer + 3,thisOp.modes[2], retval)
            pointer_increment = 4
        elif thisOp.code == 3:
            #  Read input:  3,loc
            if self.input_pointer >= len(self.input):
                # Wait for more input!
                self.status = 'Waiting for input'
                pointer_increment = 0
                willcontinue = False
            else:
                theinputvalue = self.input[self.input_pointer]
                self.input_pointer += 1
                self.storeValue(self.instruction_pointer + 1,thisOp.modes[0], theinputvalue)
                pointer_increment = 2
        elif thisOp.code == 4:
            # Write output: 4,a
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            self.output.append(val0)
            pointer_increment = 2
        elif thisOp.code == 5:
            # Jump-if-true:  5,a,b  if a then insptr=b
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            if val0 != 0:
                self.instruction_pointer = val1
            else:
                pointer_increment = 3
        elif thisOp.code == 6:
            # Jump-if-false:  6,a,b  if !a then isptr=b
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            if val0 == 0:
                self.instruction_pointer = val1
            else:
                pointer_increment = 3
        elif thisOp.code == 7:
            # less than:  7,a,b,loc   if a<b *loc=1 else *loc=0
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            retval = 0
            if val0 < val1:
                retval = 1
            self.storeValue(self.instruction_pointer + 3,thisOp.modes[2], retval)
            pointer_increment = 4
        elif thisOp.code == 8:
            # less than:  7,a,b,loc   if a=b *loc=1 else *loc=0
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            retval = 0
            if val0 == val1:
                retval = 1
            self.storeValue(self.instruction_pointer + 3,thisOp.modes[2], retval)
            pointer_increment = 4
        elif thisOp.code == 9:
            # adjust relative base
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            self.relative_base += val0
            pointer_increment = 2

                                

        else:
            #print("Halting with instruction ", iop)
            self.status = 'Halted'
            willcontinue = False

        self.instruction_pointer += pointer_increment          

        return willcontinue


if __name__ == "__main__":
    # Some tests here

    # I/O:  get input, write output, terminate
    test1 = IntCodeProgram('3,0,4,0,99')
    test1.setInput([10])
    test1.process()
    print(f"Test1 input={test1.input} output={test1.output}")
    if (test1.input[0] != test1.output[0]):
        print("Test 1: FAIL")
    
    # consider whether the input is equal to 8; output 1 (if it is) or 0 (if it is not)
    test3 = IntCodeProgram('3,9,8,9,10,9,4,9,99,-1,8')   
    test3.setInput([8])
    test3.process()
    print(f'Test3 output={test3.output}')  # if input=8, then 1

    #109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99 takes no input and produces a copy of itself as output
    test4 = IntCodeProgram('109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99')
    test4.process()
    print(f'Test4 output={test4.output}')

    #test 5  should produce a large number
    test5 = IntCodeProgram('1102,34915192,34915192,7,4,7,99,0')
    test5.process()
    print(f'Test5 output={test5.output}')
   
    #test 6 should produce the number in the middle
    test6 = IntCodeProgram('104,1125899906842624,99')
    test6.process()
    print(f'Test6 output={test6.output}')