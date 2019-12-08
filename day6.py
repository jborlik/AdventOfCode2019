
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
K)L
K)YOU
I)SAN"""

#alldata = [x.split(')') for x in testdata.splitlines()]

class Node:
    def __init__(self, name):
        self.name = name
        self.parent = None
        self.children = []
    def __str__(self):
        kidnames = ' '.join([x.name for x in self.children])
        if self.parent:
            return f'(name={self.name} p={self.parent.name} children=[{kidnames}])'
        return f'(name={self.name} p=None children=[{kidnames}])'
    def __repr__(self):
        return self.__str__()
    def countToTop(self):
        count = 0
        aparent = self.parent
        while aparent:
            count += 1
            aparent = aparent.parent
        return count
    def returnFullChain(self):
        parentlist = [self]
        if self.parent:
            parentlist.extend(self.parent.returnFullChain())
        return parentlist
    def printFullChain(self):
        fulllist = self.returnFullChain()
        print('->'.join([x.name for x in fulllist]))
    def countToAncestor(self,ancestor):
        if self == ancestor:
            return 1
        return 1 + self.parent.countToAncestor(ancestor)


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

print(f'Part 1:  Total orbits={sumorbits}')


def findCommonNode(node1, node2):
    print(f'looking at {node1.name} and {node2.name}')
    if node1.parent == node2.parent:
        return node1.parent
    if node1.parent != None:
        a1 = findCommonNode(node1.parent, node2)
        if a1 != None:
            return a1
    if node2.parent != None:
        a2 = findCommonNode(node1, node2.parent)
        if a2 != None:
            return a2
    return None

mynode = allnodes['YOU']
destnode = allnodes['SAN']

list1 = mynode.returnFullChain()
list2 = destnode.returnFullChain()
mynode.printFullChain()
destnode.printFullChain()

commonnode = None
for i in list1:
    if i in list2:
        commonnode = i
        break

print('common ancestor=',commonnode)

c1 = mynode.countToAncestor(commonnode)
c2 = destnode.countToAncestor(commonnode)
print(f'count 1={c1} count 2={c2}')
print('Part 2: orbit changes=',c1+c2-2-2)