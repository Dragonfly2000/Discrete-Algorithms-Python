def EulerPath(V,E,gT):
    Vd, start=CreateDict(V,E,gT)
    path=MainPath(Vd, start, gT)
    path=SideLoops(Vd, path, gT)
    path=path[:-1]
    return path

def CreateDict(V,E,gT):
    Vd={}
    odd=[]
    if gT=='1':
        for v in V:
            Vd[v]=[]
            count=0
            for e in E:
                if v in e:
                    p=(v,v)
                    for x in e:
                        if v!=x:
                            p=(v,x)
                    Vd[v].append(p)
                    for x in p:
                        if x==v:
                            count+=1

            if count%2!=0:
                odd.append(v)

        if len(odd)!=0 and len(odd)!=2:
            print("Eulerian Path doesn't exist!!")
            exit()

        if len(odd)>0:
            start=odd.pop(0)
        else:
            start=V[0]



    else:
        for v in V:
            Vd[v]=[]
            outC=0
            inC=0
            startLst=[]
            endLst=[]
            for e in E:
                if e[0]==v:
                    outC+=1
                    Vd[v].append(e)
                if e[1]==v:
                    inC+=1
            if outC==inC+1:
                startLst.append(v)
            elif inC==outC+1:
                endLst.append(v)
            elif outC!=inC:
                print("EulerPath doesn't exist")
                exit()
        
        if (len(startLst)!=0 and len(startLst)!=1) or (len(startLst)!=len(endLst)):
            print("Eulerian Path doesn't exist!!")
            exit()

        if len(startLst)>0:
            start=startLst.pop()
        else:
            start=V[0]

    return Vd, start

def MainPath(Vd,start,gT):
    c=start
    path=c+'-'
    while(Vd[c]!=[]):
        x, y=Vd[c].pop(0)
        if gT=='1' and y!=x:
            Vd[y].remove((y,x))
        c=y
        path+=c+'-'

    return path

def SideLoops(Vd, path,gT):
    for v in Vd:
        c=v
        loop=''
        while(Vd[c]!=[]):
            x, y=Vd[c].pop(0)
            if gT=='1' and y!=x:
                Vd[y].remove((y,x))
            c=y
            loop+=c+'-'
        i=path.index(v)
        path=path[:i+1]+loop+path[i+1:]

    return path






####################   MAIN PROG  ################################


V=[]
gT=input("Enter 1 for undirected graph\n      2 for directed graph:")
print()

inp=input("Enter vertex, enter 0 when done: ")
while(inp!='0'):
    V.append(inp)
    inp=input("Enter vertex, enter 0 when done: ")
print()

E=[]
inp=input("Enter 2 vertices of an edge (comma ',' seperated), enter 0 when done: ")
while(inp!='0'):
    x=inp[0]
    y=inp[-1]
    E.append((x,y))
    inp=input("Enter 2 vertices of an edge (comma ',' seperated), enter 0 when done: ")
print()    

print(EulerPath(V,E,gT))
