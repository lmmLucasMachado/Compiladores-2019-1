def INPP(D, s):
    s = -1
    D[0] = 0
    return D, s

def CRCT(M, s, k):
    s=s+1
#    print("print %i" % s)
    M[s] = k
    return M,s,k

def SOMA(M, s):
    M[s-1] = M[s-1]+M[s]
    s=s-1
    return M, s

def SUBT(M, s):
    M[s-1] = M[s-1]-M[s]
    s=s-1
    return M, s

def DIVI(M, s):
    M[s-1] = M[s-1]/M[s]
    s=s-1
    return M, s

def MULT(M, s):
    M[s-1] = M[s-1]*M[s]
    s=s-1
    return M, s

def INVR(M, s):
    M[s] = M[s]*(-1)
    return M, s

def NEGA(M, s):
    M[s] = 1-M[s]
    return M, s

def CONJ(M, s):
    if M[s-1]==1 and M[s]==1:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def DISJ(M, s):
    if M[s-1]==1 or M[s]==1:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMME(M, s):
    if M[s-1]<M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMMA(M, s):
    if M[s-1]>M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMIG(M, s):
    if M[s-1]==M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMDG(M, s):
    if M[s-1]!=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMAG(M, s):
    if M[s-1]>=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def CMEG(M, s):
    if M[s-1]<=M[s]:
        M[s-1]=1
    else:
        M[s-1]=0
    s=s-1
    return M, s

def DSVF(M,s, i,  p):
    if M[s] == 0:
        i = p - 1
    s = s - 1
    return M, s, i, p

def DSVS(M, i,  p):
    i = p - 1
    return M, i, p

def AMEM(M, s,  n):
    s = s + n
    return M, s, n

def DMEM(M, s,  n):
    s =s - n
    return M, s, n

def CRVL(M,D, s,  m,  n):
    s = s + 1
    M[s] = M[D[m]+n]
    return M, D, s, m, n

def ARMZ(M,D, s,  m,  n):
    M[D[m]+n] = M[s]
    s = s - 1
    return M, D, s, m, n

def IMPR(M, s):
    print(M[s])
    s = s - 1
    return M, s

def LEIT(M, s):
    s = s + 1
    n = input()

    M[s] = n
    return M, s


arq = open('arquivo.mepa', "r")
labels = []
line_label = []
final = 0
line = []


for cont, l in enumerate(arq):
    lb = []
    lb = l.split(" ")

    if lb[0] != "":
        labels.append(lb[0][0:len(lb[0])-1])
        line_label.append(cont)
        lb.pop(0)
        line.append(lb)
#        print(lb)
    else:
        while lb[0] == '':
            lb.pop(0)
        line.append(lb)

#print(line)

s=0
k=0
m=0
n=0
p=0
j=0
M = [-1]*15
D = [-1]*15

for i, line_code in enumerate(line):
    #print("o S %i" % s)

    if line_code[0].strip()=="INPP":
       D, s = INPP(D,s)
    elif line_code[0].strip()=="CRCT":
        k = int(line_code[1])
        #print(M)
        M,s,k=CRCT(M,s,k)
        #print(M)
    elif line_code[0].strip()=="SOMA":
        M,s =SOMA(M,s)

    elif line_code[0].strip()=="SUBT":
        M,s =SUBT(M,s)

    elif line_code[0].strip()=="MULT":
        M,s =MULT(M,s)

    elif line_code[0].strip()=="DIVI":
        M,s =DIVI(M,s)

    elif line_code[0].strip()=="INVR":
        M,s =INVR(M,s)

    elif line_code[0].strip()=="NEGA":
        M,s =NEGA(M,s)

    elif line_code[0].strip()=="CONJ":
        M,s =CONJ(M,s)

    elif line_code[0].strip()=="DISJ":
        M,s =DISJ(M,s)

    elif line_code[0].strip()=="CMME":
        M,s =CMME(M,s)

    elif line_code[0].strip()=="CMMA":
        M,s =CMMA(M,s)

    elif line_code[0].strip()=="CMIG":
        M,s =CMIG(M,s)

    elif line_code[0].strip()=="CMDG":
        M,s =CMDG(M,s)

    elif line_code[0].strip()=="CMAG":
        M,s =CMAG(M,s)

    elif line_code[0].strip()=="CMEG":
        M,s =CMEG(M,s)

    elif line_code[0].strip()=="DSVF":
        position = 0
        for a,o in enumerate(labels):
            if line_code[1].strip()  == o.strip():
                position = a
                break
        p = line_label[position]
        if p!=0:
            M,s,i,p =DSVF(M,s,i,p)
        else:
            print("Linha %i : RunTime error rotulo %s invalido" % (i + 1, line_code[1]))
            break

    elif line_code[0].strip()=="DSVS":
        position = 0
        for a,p in enumerate(labels):
            if line_code[1].strip()  == p.strip():
                position = a
                break
        p = line_label[position]

        if p!=0:
            M,i,p = DSVS(M,i,p)
        else:
            print("Linha %i : RunTime error rotulo %s invalido" % (i + 1, line_code[1]))
            break
        
    elif line_code[0].strip()=="AMEM":
        n = int(line_code[1])
        M,s,n=AMEM(M,s,n)

    elif line_code[0].strip()=="DMEM":
        n = int(line_code[1])
        M,s,n = DMEM(M,s,n)

    elif line_code[0].strip()=="CRVL":
        buffer = line_code[1][0:len(line_code)-2]
        m = int(buffer)
        n = int(line_code[2])
        M,D,s,m,n = CRVL(M,D,s,m,n)

    elif line_code[0].strip()=="ARMZ":
        buffer = line_code[1][0:len(line_code)-2]
        m = int(buffer)
        n = int(line_code[2])
        M,D,s,m,n = ARMZ(M,D,s,m,n)

    elif line_code[0].strip()=="IMPR":
        M,s = IMPR(M,s)

    elif line_code[0].strip()=="LEIT":
        M,s = LEIT(M,s)
