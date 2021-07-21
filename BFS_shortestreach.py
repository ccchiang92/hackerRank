    
class Graph(object):
    def __init__(self,n: int):
        self.nodes={}
        self.size=n
        for i in range(n):
            self.nodes[i]=[]
    def connect(self, a: int,b: int):
        a_connected, b_connected = self.nodes[a], self.nodes[b]
        a_connected.append(b)
        b_connected.append(a)
    def get(self,node: int):
        return self.nodes[node]
    def find_all_distances(self, start: int):
        curLevel=[]
        nextLevel=[]
        visited={}
        visited[start]=0
        for node in (self.get(start)):
            curLevel.append((node,6))
        while curLevel:
            current=curLevel.pop()
            currentNode=current[0]
            dist=current[1]
            if visited.get(currentNode, float('inf'))>dist:
                visited[currentNode]=dist
                connections=self.get(currentNode)
                for node in connections:
                    nextLevel.append((node,dist+6))
            if not curLevel:
                curLevel, nextLevel=nextLevel, curLevel
        output=''
        for i in range(self.size):
            if i!=start:
                output+=(str(visited.get(i,-1))+' ')
        print(output[:len(output)-1])
        return output
                    
t = int(input())
for i in range(t):
    n,m = [int(value) for value in input().split()]
    graph = Graph(n)
    for i in range(m):
        x,y = [int(x) for x in input().split()]
        graph.connect(x-1,y-1) 
    s = int(input())
    graph.find_all_distances(s-1)

            