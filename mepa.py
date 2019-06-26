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
    s = s - 1

def DSVS(M, i,  p):
    i = p - 1

def AMEM(M, s,  n):
    s = s + n

def DMEM(M, s,  n):
    s =s - n

def CRVL(M,D, s,  m,  n):
    s = s + 1
    M[s] = M[D[m]+n]

def ARMZ(M,D, s,  m,  n):
    M[D[m]+n] = M[s]
    s = s - 1

def IMPR(M, s):
    print(M[s])
    s = s - 1

def LEIT(M, s):
    s = s + 1
    n = input()

    M[s] = n


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
        print(lb)
    else:
        while lb[0] == '':
            lb.pop(0)
        line.append(lb)

print(line)

s=0
k=0
m=0
n=0
p=0
j=0
M = [None]*1000
D = [None]*1000

for i, line_code in enumerate(line):
        
    if line_code[0]=="INPP":
        INPP(D,s)

    elif line_code[0]=="CRCT":
        k = line_code[1][0:len(line_code[2])-2]
        CRCT(M,s,k)

    elif line_code[0]=="SOMA":
        SOMA(M,s)

    elif line_code[0]=="SUBT":
        SUBT(M,s)

    elif line_code[0]=="MULT":
        MULT(M,s)

    elif line_code[0]=="DIVI":
        DIVI(M,s)

    elif line_code[0]=="INVR":
        INVR(M,s)

    elif line_code[0]=="NEGA":
        NEGA(M,s)

    elif line_code[0]=="CONJ":
        CONJ(M,s)

    elif line_code[0]=="DISJ":
        DISJ(M,s)

    elif line_code[0]=="CMME":
        CMME(M,s)

    elif line_code[0]=="CMMA":
        CMMA(M,s)

    elif line_code[0]=="CMIG":
        CMIG(M,s)

    elif line_code[0]=="CMDG":
        CMDG(M,s)

    elif line_code[0]=="CMAG":
        CMAG(M,s)

    elif line_code[0]=="CMEG":
        CMEG(M,s)

    elif line_code[0]=="DSVF":
        position = 0
        for a,o in enumerate(labels):
            if line_code[2][0:len(line_code[2])-2] == o[0]:
                position = a
                break
        p = line_label[position]
        if p!=0:
            DSVF(M,s,i,p)
        else:
            print("Linha %s : RunTime error rotulo %s invalido" % (i, line_cone[2][0:len(line_code[2])-2]))
            break

    elif line_code[0]=="DSVS":
        position = 0
        for a,o in enumerate(labels):
            if line_code[2][0:len(line_code[2])-2] == o:
                position = a
                break
        p = line_label[position]

        if p!=0:
            DSVS(M,i,p)
        else:
            print("Linha %i : RunTime error rotulo %i invalido" % (i, line_cone[2][0:len(line_code[2])-2]))
            break
        
    elif line_code[0]=="AMEM":
        n = int(line_code[1][0:len(line_code[1])-2])
        AMEM(M,s,n)

    elif line_code[0]=="DMEM":
        n = int(line_code[1][0:len(line_code[1])-2])
        DMEM(M,s,n)

    elif line_code[0]=="CRVL":
        m = int(line_code[1][0:len(line_code[1])-1])
        n = int(line_code[2][0:len(line_code[2])-2])
        CRVL(M,D,s,m,n)

    elif line_code[0]=="ARMZ":
        m = int(line_code[1][0:len(line_code[1])-1])
        n = int(line_code[2][0:len(line_code[2])-2])
        ARMZ(M,D,s,m,n)

    elif line_code[0]=="IMPR":
        IMPR(M,s)

    elif line_code[0]=="LEIT":
        LEIT(M,s)
