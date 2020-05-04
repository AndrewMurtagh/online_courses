# Uses python3

"""

  _ s h o r t
_ 0 0 0 0 0 0
p 0 . . . . .
o 0 . . . . .
r 0 . . . . .
t 0 . . . . .
s 0 . . . . .
a 0 . . . . .

"""
def edit_distance(from_s, to_s):
    if from_s==to_s:
        return 0
    len_from = len(from_s)+1
    len_to = len(to_s)+1

    table={}
    for i in range(len_from):
        table[i,0]=i
    for j in range(len_to):
        table[0,j]=j

    for i in range(1,len_from):
        for j in range(1,len_to):
            if from_s[i-1] == to_s[j-1]:
                table[i,j] = table[i-1,j-1]
            else:
                table[i,j] = 1+min(table[i,j-1], table[i-1,j], table[i-1,j-1])
    return table[len_from-1, len_to-1]



if __name__ == "__main__":
    # print(edit_distance("ab", "ab"))
    # print(edit_distance("st", "ports"))
    # print(edit_distance("short", "ports"))
    # print(edit_distance("editing", "distance"))
    print(edit_distance(input(), input()))
