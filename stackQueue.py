
class stackQueue(object):
    def __init__(self):
        self.oldest=[]
        self.newest=[]
    def peek(self):
        if self.oldest==[]:
            while self.newest:
                self.oldest.append(self.newest.pop())
        if self.oldest:
            return self.oldest[-1]
        else:
            return None
    def pop(self):
        if self.oldest==[]:
            while self.newest:
                self.oldest.append(self.newest.pop())
        if self.oldest:
            return self.oldest.pop()
        else:
            return None
    def put(self, value):
        self.newest.append(value)
        
n=int(input())
queries=[]
for i in range(n):
    queries.append(input().split())
newQ=stackQueue()
for q in queries:
    if q[0]=='1':
        newQ.put(q[1])
    elif q[0]=='2':
        newQ.pop()
    elif q[0]=='3':
        print(newQ.peek())
