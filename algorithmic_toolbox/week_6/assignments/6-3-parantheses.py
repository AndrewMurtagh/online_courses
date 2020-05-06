# Uses python3
def eval(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False




def get_maximum_value(dataset):


    def minandmax(i, j):

        curr_min=1e12
        curr_max=-1e12
        for k in range(i, j):
            a = eval(M[i][k], ops[k], M[k+1][j])
            b = eval(M[i][k], ops[k], m[k+1][j])
            c = eval(m[i][k], ops[k], M[k+1][j])
            d = eval(m[i][k], ops[k], m[k+1][j])

            curr_min = min(curr_min, a, b, c, d)
            curr_max = max(curr_max, a, b, c, d)
        return curr_min, curr_max


    n = (len(dataset)-1)//2
    ops = []
    for c in dataset:
        if c =="+" or c=="-" or c=="*":
            ops.append(c)

    M = [ [0 for _ in range(n+1) ] for _ in range(n+1)]
    m = [ [0 for _ in range(n+1) ] for _ in range(n+1)]

    for i in range(0,2*n+2,2):
        M[i//2][i//2] = int(dataset[i])
        m[i//2][i//2] = int(dataset[i])

    for s in range(1, n+1):
        for i in range(n-s+1):
          j = i+s
          m[i][j], M[i][j] = minandmax(i,j)


    return M[0][n]

if __name__ == "__main__":
    # print(get_maximum_value("1+5"))
    # print(get_maximum_value("5-8+7*4-8+9"))

    print(get_maximum_value(input()))
