class MyQueue(object):
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
        

queue = MyQueue()
t = int(input())
for line in range(t):
    values = map(int, input().split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])        
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
