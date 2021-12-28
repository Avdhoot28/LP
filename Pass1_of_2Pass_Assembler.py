import fileinput


Machine_Opcode_Table = {
    'STOP':('IS', '00'),
    'ADD':('IS', '01'),
    'SUB':('IS', '02'),
    'MULT':('IS', '03'),
    'MOVER':('IS', '04'),
    'MOVEM':('IS', '05'),
    'COMP':('IS', '06'),
    'BC':('IS', '07'),
    'DIV':('IS', '08'),
    'READ':('IS', '09'),
    'PRINT':('IS', '10'),
    'START':('AD', '01'),
    'END':('AD', '02'),
    'ORIGIN':('AD', '03'),
    'EQU':('AD', '04'),
    'LTORG':('AD', '05'),
    'DS':('DL', '01'),
    'DC':('DL', '02'),
    'AREG':('RG','01'),
    'BREG':('RG','02'),
    'CREG':('RG','03'),
    'DREG':('RG','04'),
    'LT':('CC','01'),
    'LE':('CC','02'),
    'EQ':('CC','03'),
    'GT':('CC','04'),
    'GE':('CC','05'),
    'ANY':('CC','06'),
}

Intermediate_Code = []
Symbol_Table = {}
index_for_Symbol_table = 1
Literal_Table = {}
Pool_Table = [0]

Location_Count = 0
line_count = 0
Pool_table_count = 0

for line in fileinput.input(files ='input_Pass1.txt'):
	line = line.rstrip("\n")
	List = line.split(" ")
	try:
		List.remove('')
	except ValueError:
		pass
	# print(List)
	Line_Intermediate_Code = []
	LTORG = 0

	if(List[0] == 'START'):
		Location_Count = int(List[1]) - 1
	if(List[0] == 'LTORG'):
		for i in Literal_Table:
			if(Literal_Table[i] == '-1'):
				Literal_Table[i] = Location_Count
				a = i[1:]
				a = a.rstrip("\'")
				a = a.lstrip("\'")
				Line_Intermediate_Code.append(('DL','01'))
				Line_Intermediate_Code.append(('C', a))
				Location_Count+=1
				Pool_table_count+=1
		Pool_Table.append(Pool_table_count)
		LTORG = 1
	if(List[0] == 'ORIGIN'):
		change_location_to = List[1].split()
		Location_Count = Symbol_Table[change_location_to[0]] + int(change_location_to[1])
	try:
		if(List[1] == 'ORIGIN'):
			Symbol_Table[List[0]] = Symbol_Table[List[2]]
	except IndexError:
		pass
	if(LTORG == 0):
		if(List[0] not in Machine_Opcode_Table):
			Symbol_Table[List[0]] = Location_Count
		else:
			Line_Intermediate_Code.append(Machine_Opcode_Table[List[0]])
		
		try:
			# List[1]
			if(List[1] not in Machine_Opcode_Table):
				try:
					if(isinstance(int(List[1]), int)):
						Line_Intermediate_Code.append(('C',int(List[1])))
				except ValueError:
					pass
				if('=' in List[1]):
					Literal_Table[List[1]] = '-1'
				elif(List[1] not in Symbol_Table and Line_Intermediate_Code[-1][0] != 'C'):
					Symbol_Table[List[1]] = -1
					Line_Intermediate_Code.append(('S',index_for_Symbol_table))
					index_for_Symbol_table+=1
			else:
				Line_Intermediate_Code.append(Machine_Opcode_Table[List[1]])
		except IndexError:
			pass

		try:
			# List[2]
			if(List[2] not in Machine_Opcode_Table):
				try:
					if(isinstance(int(List[2]), int)):
						Line_Intermediate_Code.append(('C',int(List[2])))
				except ValueError:
					pass
				if('=' in List[2]):
					Literal_Table[List[2]] = '-1'
				elif(List[2] not in Symbol_Table and Line_Intermediate_Code[-1][0] != 'C'):
					Symbol_Table[List[1]] = -1
					Line_Intermediate_Code.append(('S',index_for_Symbol_table))
					index_for_Symbol_table+=1
			else:
				Line_Intermediate_Code.append(Machine_Opcode_Table[List[2]])
		except IndexError:
			pass

	Intermediate_Code.append(Line_Intermediate_Code)
	line_count+=1
	Location_Count+=1


# print(Symbol_Table)
print()
print("Intermediate Code - ")
print()
for i in Intermediate_Code:
    print(i)
print()
print("Symbol Table - ")
print()
for i in Symbol_Table:
    print(i, Symbol_Table[i])
print()
print("Literal Table - ")
print()
for i in Literal_Table:
    print(i, Literal_Table[i])
print()
print("Pool Table - ")
print()
for i in Pool_Table:
    print(i)
print()