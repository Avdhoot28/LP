# FCFS

processes = []
n = int(input("Please enter the total number of processes - "))
for i in range(n):
    processes.append(i+1)

burst_time = []


for i in range(n):
    print("Enter the burst time for ", i+1, " - ")
    a = int(input())
    burst_time.append(a)



def findavgTime( processes, n, bt):

	wt = [0] * n
	tat = [0] * n
	total_wt = 0
	total_tat = 0

	findWaitingTime(processes, n, bt, wt)

	findTurnAroundTime(processes, n,
					bt, wt, tat)

	print( " Waiting time " )

	for i in range(n):
	
		total_wt = total_wt + wt[i]
		total_tat = total_tat + tat[i]
		print(" " + str(wt[i]) )

	print( "Average waiting time = "+
				str(total_wt / n))
	print("Average turn around time = "+
					str(total_tat / n))

def findTurnAroundTime(processes, n,
					bt, wt, tat):

	for i in range(n):
		tat[i] = bt[i] + wt[i]

def findWaitingTime(processes, n,
					bt, wt):

	wt[0] = 0

	for i in range(1, n ):
		wt[i] = bt[i - 1] + wt[i - 1]



findavgTime(processes, n, burst_time)



# SJF


# processes = []
# n = int(input("Please enter the total number of processes - "))
# for i in range(n):
#     processes.append(i+1)

# burst_time = []
# input_time = []
# arr = []

# for i in range(n):
#     print("Enter the burst time for ", i+1, " - ")
#     a = int(input())
#     burst_time.append(a)

# for i in range(n):
#     print("Enter the arrival time for ", i+1, " - ")
#     a = int(input())
#     input_time.append(a)

# arr = [processes, input_time, burst_time, [0]*n, [0]*n, [0]*n]



# def arrangeArrival(n, array):
# 	for i in range(0, n):
# 		for j in range(i, n-i-1):
# 			if array[1][j] > array[1][j+1]:
# 				for k in range(0, n):
# 					array[k][j], array[k][j+1] = array[k][j+1], array[k][j]


# def CompletionTime(n, array):
# 	value = 0
# 	array[3][0] = array[1][0] + array[2][0]
# 	array[5][0] = array[3][0] - array[1][0]
# 	array[4][0] = array[5][0] - array[2][0]
# 	for i in range(1, n):
# 		temp = array[3][i-1]
# 		mini = array[2][i]
# 		for j in range(i, n):
# 			if temp >= array[1][j] and mini >= array[2][j]:
# 				mini = array[2][j]
# 				value = j
# 		array[3][value] = temp + array[2][value]
# 		array[5][value] = array[3][value] - array[1][value]
# 		array[4][value] = array[5][value] - array[2][value]
# 		for k in range(0, 6):
# 			array[k][value], array[k][i] = array[k][i], array[k][value]



# arrangeArrival(n, arr)
# CompletionTime(n, arr)
# print("Burst \tCompletion \tWaiting")
# waitingtime = 0
# turaroundtime = 0
# for i in range(0, n):
#     print(arr[2][i],
#         "\t\t", arr[3][i], "\t\t", arr[4][i])
#     waitingtime += arr[4][i]
#     turaroundtime += arr[5][i]
# print("Average waiting time is ", (waitingtime/n))
# print("Average Turnaround Time is ", (turaroundtime/n))


# Priority


# processes = []
# n = int(input("Please enter the total number of processes - "))
# for i in range(n):
#     processes.append(i+1)


# arrivaltime = []
# bursttime = []
# priority = []

# for i in range(n):
#     print("Enter the burst time for ", i+1, " - ")
#     a = int(input())
#     bursttime.append(a)

# for i in range(n):
#     print("Enter the arrival time for ", i+1, " - ")
#     a = int(input())
#     arrivaltime.append(a)

# for i in range(n):
#     print("Enter the priorities for ", i+1, " - ")
#     a = int(input())
#     priority.append(a)



# totalprocess = n
# proc = []
# for i in range(n):
# 	l = []
# 	for j in range(n-1):
# 		l.append(0)
# 	proc.append(l)

# for i in range(totalprocess):

#     proc[i][0] = arrivaltime[i]
#     proc[i][1] = bursttime[i]
#     proc[i][2] = priority[i]
#     proc[i][3] = i + 1

# proc = sorted (proc, key = lambda x:x[2])
# proc = sorted (proc)

# def get_wt_time( wt):

# 	service = [0] * 5

# 	service[0] = 0
# 	wt[0] = 0

# 	for i in range(1, totalprocess):
# 		service[i] = proc[i - 1][1] + service[i - 1]
# 		wt[i] = service[i] - proc[i][0] + 1

# 		if(wt[i] < 0) :	
# 			wt[i] = 0
		
# def get_tat_time(tat, wt):

# 	for i in range(totalprocess):
# 		tat[i] = proc[i][1] + wt[i]

# def findgc():
	
# 	wt = [0] * 5
# 	tat = [0] * 5

# 	wavg = 0
# 	tavg = 0

# 	get_wt_time(wt)
	
# 	get_tat_time(tat, wt)

# 	stime = [0] * 5
# 	ctime = [0] * 5
# 	stime[0] = 1
# 	ctime[0] = stime[0] + tat[0]
	
# 	for i in range(1, totalprocess):
# 		stime[i] = ctime[i - 1]
# 		ctime[i] = stime[i] + tat[i] - wt[i]



# 	for i in range(totalprocess):
# 		wavg += wt[i]
# 		tavg += tat[i]
		


# 	print("Average waiting time is : ", end = " ")
# 	print(wavg / totalprocess)
# 	print("average turnaround time : " , end = " ")
# 	print(tavg / totalprocess)




# findgc()




