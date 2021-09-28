n=int(input())
ops=[]
for i in range(n):
    raw=input()
    ops.append((int(raw[0]),raw[2:]))
outputString=''
undoList=[]
for op in ops:
    if op[0]==1:
        outputString+=op[1]
        undoList.append(('add',len(op[1])))
    elif op[0]==2:
        k=int(op[1])
        undoList.append(('del',outputString[-k:]))
        outputString=outputString[0:-k]
    elif op[0]==3:
        print(outputString[int(op[1])-1])
    elif op[0]==4:
        last=undoList.pop()
        if last[0]=='add':
            k=last[1]
            outputString=outputString[0:-k]
        else:
            outputString+=last[1]