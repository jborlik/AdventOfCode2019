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
        self.memory = [int(x) for x in programline.split(sep=',')]
        self.instruction_pointer = 0
        self.input = []
        self.input_pointer = 0
        self.output = []

    def setInput(self, theinput):
        self.input = theinput

    def process(self):
        iscontinuing = True
        while iscontinuing:
            iscontinuing = self.processNextInstructionAndContinue()

    def resolveValue(self, parameter, mode):
        if mode == '0':
            return self.memory[parameter]
        if mode == '1':
            return parameter
        return 0

    def processNextInstructionAndContinue(self):
        thisOp = OpCode(self.memory[self.instruction_pointer])
        pointer_increment = 0
        willcontinue = True

        if thisOp.code == 1:
            #  Addition:  1,a,b,loc
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            ilocput = self.memory[self.instruction_pointer + 3]
            retval = val0 + val1
            self.memory[ilocput] = retval
            pointer_increment = 4
        elif thisOp.code == 2:
            #  Multiplication:  2,a,b,loc
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            ilocput = self.memory[self.instruction_pointer + 3]
            retval = val0 * val1
            self.memory[ilocput] = retval
            pointer_increment = 4
        elif thisOp.code == 3:
            #  Read input:  3,loc
            theinputvalue = self.input[self.input_pointer]
            self.input_pointer += 1
            ilocput = self.memory[self.instruction_pointer + 1]
            self.memory[ilocput] = theinputvalue
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
            ilocput = self.memory[self.instruction_pointer + 3]
            self.memory[ilocput] = 0
            if val0 < val1:
                self.memory[ilocput] = 1
            pointer_increment = 4
        elif thisOp.code == 8:
            # less than:  7,a,b,loc   if a=b *loc=1 else *loc=0
            val0 = self.resolveValue(self.memory[self.instruction_pointer+1], thisOp.modes[0])
            val1 = self.resolveValue(self.memory[self.instruction_pointer+2], thisOp.modes[1])
            ilocput = self.memory[self.instruction_pointer + 3]
            self.memory[ilocput] = 0
            if val0 == val1:
                self.memory[ilocput] = 1
            pointer_increment = 4
                                

        else:
            #print("Halting with instruction ", iop)
            willcontinue = False

        self.instruction_pointer += pointer_increment          

        return willcontinue


