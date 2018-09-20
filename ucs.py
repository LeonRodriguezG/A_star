from copy import deepcopy

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

IniNode = Node((0,0),IniS,0)
Tie = 0
q.put((IniNode.cost,Tie,IniNode))
PoppedNode = Node((0,0),IniS,0)
Visited = []
Visited.append(IniS)

#We assume that the # of containers is the same in both the initial state and the goal state

for x in range(0, LenStack):
    if(not(len(IniS[x]) <= int(Max))):
        print("No solution found")
        exit()
    if(not(len(GS[x]) <= int(Max))):
        print("No solution found")
        exit()

for x in range(0, LenStack): 
    for y in range(0, len(IniS[x])):
        if(IniS[x][y] == ''):
            del(IniS[x][len(IniS[x]) - 1])
    for y in range(0, len(GS[x])):
        if(GS[x][y] == ''):
            del(GS[x][len(GS[x]) - 1])

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
                        NewState[y].append(Stack[x][len(Stack[x]) - 1])
                        del(NewState[x][len(NewState[x]) - 1])

                        AlVisited=False
                        for Vis in Visited:
                            if(NewState==Vis):
                                AlVisited=True
                        if not AlVisited:
                            NewCost=abs(x - y) + DefCost + PoppedNode.cost
                            AuxNode=Node((x,y),NewState,NewCost)
                            AuxNode.father = PoppedNode
                            q.put((NewCost,Tie,AuxNode))
                            Visited.append(NewState)
        PoppedNode = q.get()[2]

if Compare(PoppedNode.state,GS):
    print(PoppedNode.cost)
    states_recursion(PoppedNode)
    text = ""
    for x in range(0, len(temp)):
            text += str(temp.pop()) + "; "
    text = text[:-2]
    print(text)