from copy import deepcopy
from random import randrange

try:
    import Queue as Q  # ver. < 3.0
except ImportError:
    import queue as Q

class Node:
    def __init__ (self,action,state,cost):
        self.father = None
        self.action = action
        self.state  = state
        self.cost   = cost

def Compare(S1,S2):
    f = True
    for x in range(0, LenStack):
        try:
            if S2[x][0] != "X":
                if S2[x]!=S1[x]:
                    f=False
        except: 
            if S2[x] != "X":
                if S2[x]!=S1[x]:
                    f=False
    return f

def states_recursion(actual):
  if(actual.father != None):
    temp.append(actual.action)
    states_recursion(actual.father)

def h(State):
    AuxMat=deepcopy(State)
    for x in range(0,LenStack):
        MaxInStack=len(AuxMat[x])
        for y in range(MaxInStack,int(Max)):
            AuxMat[x].append(0)
    AuxGS=deepcopy(GS)
    for x in range(0,LenStack):
        MaxInStack=len(AuxGS[x])
        for y in range(MaxInStack,int(Max)):
            AuxGS[x].append(0)
    heuristic=0
    for x in range(0,LenStack):
        for y in range(0,int(Max)):
            if AuxMat[x][y] != AuxGS[x][y]:
                if AuxMat[x][y] != 0:
                    if AuxGS[x][0]!='X':
                        #print("X=" + str(x) + " Y=" + str(y) + " H=" + str(heuristic))
                        heuristic+=1
    return heuristic

q = Q.PriorityQueue()

DefCost = 1
temp = []

Max = input()

InitialS = input()
IniS = InitialS.replace(" ","").split(';')
for x in range(0, len(IniS)):
    IniS[x] = IniS[x].replace("(","").replace(")","")
    IniS[x] = IniS[x].split(',')

GoalS = input()
GS = GoalS.replace(" ","").split(';')
LenStack = len(GS)
for x in range(0, len(GS)):
    GS[x] = GS[x].replace("(","").replace(")","")
    GS[x] = GS[x].split(',')

for x in range(0, LenStack): 
    for y in range(0, len(IniS[x])):
        if(IniS[x][y] == ''):
            del(IniS[x][len(IniS[x]) - 1])
    for y in range(0, len(GS[x])):
        if(GS[x][y] == ''):
            del(GS[x][len(GS[x]) - 1])

IniNode = Node((0,0),IniS,h(IniS))
Tie = 0
q.put((IniNode.cost,Tie,IniNode))
PoppedNode = Node((0,0),IniS,h(IniS))

#We assume that the # of containers is the same in both the initial state and the goal state

for x in range(0, LenStack):
    if(not(len(IniS[x]) <= int(Max))):
        print("No solution found")
        exit()
    if(not(len(GS[x]) <= int(Max))):
        print("No solution found")
        exit()

while (not Compare(PoppedNode.state, GS)) and (not q.empty()):
    if (Tie == 0):
        PoppedNode = q.get()[2]
    if not Compare(PoppedNode.state,GS):
        Stack=deepcopy(PoppedNode.state)
        for x in range(0,LenStack):
            if len(Stack[x]) > 0:
                for y in range(0,LenStack):
                    if x != y and len(Stack[y]) < int(Max):
                        NewState = deepcopy(Stack)
                        Tie += 1
                        ran = randrange(4)
                        NewState[y].append(Stack[x][len(Stack[x]) - 1])
                        del(NewState[x][len(NewState[x]) - 1])
                        NewCost=abs(x - y) + DefCost + PoppedNode.cost + h(NewState) - h(PoppedNode.state) + ran
                        AuxNode=Node((x,y),NewState,NewCost)
                        AuxNode.father = PoppedNode
                        q.put((NewCost,Tie,AuxNode))
        PoppedNode = q.get()[2]

if Compare(PoppedNode.state,GS):
    print(PoppedNode.cost)
    states_recursion(PoppedNode)
    text = ""
    for x in range(0, len(temp)):
            text += str(temp.pop()) + "; "
    text = text[:-2]
    print(text)