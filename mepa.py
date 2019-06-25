arq = open('arquivo.mepa', "r")
labels = []
line_label = []
final = 0
line = []

for cont, l in enumerate(arq):
    lb = []
    lb = l.split(" ")

    if lb[0] != "":
        labels = lb[0]
        line_label.append(cont)
        lb.pop(0)
        line.append(lb)
        print(lb)
    else:
        while lb[0] == '':
            lb.pop(0)
        line.append(lb)

print(line)

def INPP(D, s):
    s = -1
    D[0] = 0

def CRCT(M, s, k):
    s+=1
    M[s] = k

def SOMA(M, s):
    M[s-1] = M[s-1]+M[s]
    s-=1

def SUBT(M, s):
    M[s-1] = M[s-1]-M[s]
    s-=1

def DIVI(M, s):
    M[s-1] = M[s-1]/M[s]
    s-=1

def MULT(M, s):
    M[s-1] = M[s-1]*M[s]
    s-=1

def INVR(M, s):
    M[s] = M[s]*(-1)

def NEGA(M, s):
    M[s] = 1-M[s]

def CONJ(M, s):
    if M[s-1]==1 and M[s]==1:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def DISJ(M, s):
    if M[s-1]==1 or M[s]==1:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1


def CMME(M, s):
    if M[s-1]<M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def CMMA(M, s):
    if M[s-1]>M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def CMIG(M, s):
    if M[s-1]==M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def CMDG(M, s):
    if M[s-1]!=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def CMAG(M, s):
    if M[s-1]>=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def CMEG(M, s):
    if M[s-1]<=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s-=1

def DSVF(M,s, i,  p):
    if M[s] == 0:
        i = p - 1
    s -= 1

def DSVS(M, i,  p):
    i = p - 1

def AMEM(M, s,  n):
    s += n

def DMEM(M, s,  n):
    s -= n

def CRVL(M,D, s,  m,  n):
    s += 1
    M[s] = M[D[m]+n]

def ARMZ(M,D, s,  m,  n):
    M[D[m]+n] = M[s]
    s -= 1

def IMPR(M, s):
    print(M[s])
    s -= 1

def LEIT(M, s):
    s += 1
    n = input()

    M[s] = n

