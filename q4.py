x = eval(input('enter matrix(as a list of lists):'))
t=[]
row = len(x)
column=len(x[0])
for i in range(column):
    t.append([0]*row)
for i in range(row):
    for j in range(column):
        t[j][i]=x[i][j]
for row in t:
    print(row)
