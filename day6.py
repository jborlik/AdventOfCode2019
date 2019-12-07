
with open('day6.dat') as datafile:
    alldata = [x.strip().split(')') for x in datafile.readlines()]

testdata = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

#alldata = [x.split(')') for x in testdata.splitlines()]

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    def __str__(self):
        kidnames = ' '.join([x.name for x in self.children])
        if self.parent:
            return f'(p={self.parent.name} children=[{kidnames}])'
        return f'(p=None children=[{kidnames}])'
    def __repr__(self):
        return self.__str__()
    def countToTop(self):
        count = 0
        aparent = self.parent
        while aparent:
            count += 1
            aparent = aparent.parent
        return count
        


allnodes = {}

def getnode(nodes, nodename):
    if nodename in nodes:
        return nodes[nodename]
    newnode = Node(nodename)
    nodes[nodename] = newnode
    return newnode

for aorbit in alldata:
    print(aorbit)
    parentNode = getnode(allnodes, aorbit[0])
    childNode = getnode(allnodes, aorbit[1])
    parentNode.children.append(childNode)
    childNode.parent = parentNode

print(allnodes)

sumorbits = 0
for anode in allnodes.values():
    sumorbits += anode.countToTop()

print(f'Total orbits={sumorbits}')
