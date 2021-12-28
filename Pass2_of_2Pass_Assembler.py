import fileinput
from typing import Literal

Symbol_Table = []
Literal_Table = []


for line in fileinput.input(files ='SymTab_for_Pass2.txt'):
    A = line.split(" ")
    Symbol_Table.append((A[0],A[1]))

print(Symbol_Table)
print()

Machine_Code = []
Location_Counter = []

for line in fileinput.input(files ='IC_for_Pass2.txt'):
    line = line.rstrip("\n")
    A = line.split(" ")
    for i in range(len(A)):
        A[i]=A[i].lstrip("(")
        A[i]=A[i].rstrip(")")
        A[i]=A[i].split(",")
    # print(A)
    line_Machine_Code = []
    if(A[0]==["AD",'01'] or A[0]==["DL",'02'] or A[0]==["AD",'02'] or A[0]==["AD",'03']):
        continue
    if(A[0]==["AD",'05']):
        line_Machine_Code.append(0)
        line_Machine_Code.append(0)
        line_Machine_Code.append((A[2][2]))
        continue
    if(A[0]==["IS",'00']):
        print("came here in IS")
        line_Machine_Code.append(0)
        line_Machine_Code.append(0)
        line_Machine_Code.append(0)
        continue
    if(A[0]==["DL",'01']):
        line_Machine_Code.append(0)
        line_Machine_Code.append(0)
        line_Machine_Code.append((A[1][1]))
    if(A[0][0]=="IS"):
        line_Machine_Code.append(A[0][1])
    if(A[1][0]!="RG"):
        line_Machine_Code.append(0)
        if(A[1][0]=="C"):
            line_Machine_Code.append(A[1][0])
        elif(A[1][0]=="S"):
            line_Machine_Code.append(Symbol_Table[int(A[1][1])-1][1])
        elif(A[1][0]=="L"):
            line_Machine_Code.append(Literal_Table[int(A[1][1])-1][1])
    else:
        line_Machine_Code.append(A[1][1])
    try:
        if(A[2][0]=="C"):
            line_Machine_Code.append(A[2][0])
        elif(A[2][0]=="S"):
            line_Machine_Code.append(Symbol_Table[int(A[2][1])-1][1])
        elif(A[2][0]=="L"):
            line_Machine_Code.append(Literal_Table[int(A[2][1])-1][1])
    except IndexError:
        continue
    
    Machine_Code.append(line_Machine_Code)

print()
for i in Machine_Code:
    print(i)
print()