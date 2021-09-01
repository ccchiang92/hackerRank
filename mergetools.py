def merge_the_tools(string, k):
    if len(string)%k !=0:
        return 'Error'
    factor_list=[]
    for i in range(len(string)):
        if i==0:
            current=string[i]
            count=k-1
            used_char={}
            used_char[string[i]]=True
        elif count>0:
            count-=1
            if not used_char.get(string[i],False):
                current=current+string[i]
                used_char[string[i]]=True
        if count==0:
            factor_list.append(current)
            current=''
            count=k
            used_char={}
    for word in factor_list:
        print(word)

if __name__ == '__main__':