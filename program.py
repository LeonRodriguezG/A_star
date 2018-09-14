
Max=input()

InitialS = input()
IniS=InitialS.replace(" ","").split(';')
for x in range(0, len(IniS)):
    IniS[x]=IniS[x].replace("(","").replace(")","")
    IniS[x]=IniS[x].split(',')

GoalS= input()
GS=GoalS.replace(" ","").split(';')
for x in range(0, len(GS)):
    GS[x]=GS[x].replace("(","").replace(")","")
    GS[x]=GS[x].split(',')
