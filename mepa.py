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