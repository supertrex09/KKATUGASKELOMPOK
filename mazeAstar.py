from pyamaze import maze,agent,COLOR,textLabel
from queue import PriorityQueue
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2
    return abs(x1-x2) + abs(y1-y2)

def aStar(m):
    start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,(1,1))
    searchPath=[start]

    open=PriorityQueue()
    open.put((f_score[start],h(start,(1,1)),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        searchPath.append(currCell)
        if currCell==(1,1):
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,(1,1))

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_f_score
                    open.put((temp_f_score,h(childCell,(1,1)),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=(1,1)
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return searchPath,aPath,fwdPath

m=maze(5,5)
m.CreateMaze(loadMaze='maze.csv')
searchPath,aPath,fwdPath=aStar(m)

a=agent(m,footprints=True,color=COLOR.blue,filled=True)
b=agent(m,1,1,footprints=True,color=COLOR.yellow,filled=True,goal=(m.rows,m.cols))
c=agent(m,footprints=True,color=COLOR.red)

m.tracePath({a:searchPath},delay=300)
m.tracePath({b:aPath},delay=300)
m.tracePath({c:fwdPath},delay=300)

l=textLabel(m,'A Star Path Length',len(fwdPath)+1)
l=textLabel(m,'A Star Search Length',len(searchPath))
m.run()
