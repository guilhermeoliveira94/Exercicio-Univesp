N = 4
X = 3

A = 2
RESP = X

while A <= N:

    EXP = X\a
    B = 1

    while B < A:
        EXP = EXP * X
        B = B + 1
    else:
        RESP = RESP + EXP
        A = A+2

else:
    print(RESP)