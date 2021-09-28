def minion_game(string):
    vowels=['A','E','I','O','U']
    size=len(string)
    s_points=0
    k_points=0
    for i in range(size):
        cur_points=size-i
        if string[i] in vowels:
            k_points+=cur_points
        else:
            s_points+=cur_points
    if s_points>k_points:
        print(f"Stuart {s_points}")
    elif s_points<k_points:
        print(f"Kevin {k_points}")
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)