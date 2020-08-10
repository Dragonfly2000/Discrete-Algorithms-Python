def ShortPath(V,E,start,end,gT):
    Vd,Ed=CreateDict(V,E,gT)
    c=start
    Vd[start]=[0,start]
    length=0
    path=start
    
    while(c!=end):
        Vd=Update(Vd,Ed,c)
        c, length, path=NewC(Vd)

    return length, path

def CreateDict(V,E,gT):
    Vd={}
    Ed={}
    for v in V:
        Vd[v]=['I','']

    if(gT=='1'):
        for e in E:
            x,y = e
            Ed[(x,y)]=E[e]
            Ed[(y,x)]=E[e]
    else:
        Ed=E
    return Vd, Ed

def Update(Vd,Ed,c):
    for v in Vd:
        if(Vd[v][0]!='T' and (c,v) in Ed):
            if(Ed[(c,v)]!='I' and (Vd[v][0]=='I' or Vd[v][0]>Vd[c][0]+Ed[(c,v)])):
                Vd[v][0]=Vd[c][0]+Ed[(c,v)]
                Vd[v][1]=Vd[c][1]+v

    Vd[c][0]='T'
    return Vd

def NewC(Vd):
    flag=True
    for v in Vd:
        if Vd[v][0]!='I' and Vd[v][0]!='T':
            flag=False
            small=v
            break
    if flag:
        print("Disconnected!!")
        exit()

    for v in Vd:
        if Vd[v][0]!='I' and Vd[v][0]!='T':
            if Vd[small][0]>Vd[v][0]:
                small=v

    return small, Vd[small][0], Vd[small][1]




############# MAIN PROG #################################################

gT=input("Enter (1) for undirected graph\n      (2) for directed graph: ")
print()

V=[]
inp=input("Enter Vertex (enter 0 for completion): ")
while(inp!='0'):
    V.append(inp)
    inp=input("Enter Vertex (enter 0 for completion): ")

start=input("\nEnter the starting vertex: ")
end=input("Enter the end vertex: ")
print()
    
E={}
if gT=='1':
    i=0;
    while i<len(V):
        j=i+1
        while j<len(V):
            inp=input("Enter the length of the edge (%c,%c) ('I' if they are disconnected):" % (V[i],V[j]))
            if inp.isnumeric():
                E[(V[i],V[j])]=int(inp)
            else:
                if inp!='I':
                    print("\nInvalid input!! Enter Again\n")
                    continue
                E[(V[i],V[j])]=inp
            j+=1
        i+=1

else :
    i=0;
    while i<len(V):
        j=0
        while j<len(V):
            if i!=j:
                inp=input("Enter the length of the edge (%c,%c) ('I' if they are disconnected):" % (V[i],V[j]))
                if inp.isnumeric():
                    E[(V[i],V[j])]=int(inp)
                else:
                    if inp!='I':
                        print("\nInvalid input!! Enter Again\n")
                        continue
                    E[(V[i],V[j])]=inp
            j+=1
        i+=1



length, path=ShortPath(V,E,start,end,gT)
print("\nThe Path is:",path)
print("The Length is:",length)











