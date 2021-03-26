def commonChild(s1, s2):
    matrix =[[0]*(len(s1)+1)for i in range(len(s2)+1)]
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i]==s2[j]:
                matrix[i+1][j+1]=matrix[i][j]+1
            else:
                matrix[i+1][j+1]=max(matrix[i+1][j],matrix[i][j+1])                
    return matrix[len(s1)][len(s2)]


s1 = input()

s2 = input()

result = commonChild(s1, s2)
print(result)