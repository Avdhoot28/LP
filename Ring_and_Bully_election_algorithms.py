# Bully

number_of_processes = int(input("Enter the number of processes - "))
processes = {}
for i in range(number_of_processes):
    name = input("Enter the name of process - ")
    id = int(input("Enter the priority of process - "))
    processes[name] = id
print()
Max = 0
Max_name = ""
for i in processes:
    print(i, processes[i])
    if(processes[i]>Max):
        a = "process "+i+" is selected as the coordinator!"
        Max = processes[i]
        Max_name = i

print()
print(a)

while(True):
    print("1. Initiate a election")
    print("2. Exit")
    a = int(input())
    if(a==1):
        b = input("Enter the name of process to initiate the election from - ")
        for i in processes:
            if(processes[i]>processes[b]):
                print(b,"sends election message to", i)
        processes.pop(Max_name)
        Max_name = ""
        Max = 0
        now_remaining = []
        for i in processes:
            if(processes[i]>processes[b]):
                now_remaining.append(i)
                print(i,"sends OK message to", b)
        for j in range(len(now_remaining)):
            if(processes[now_remaining[j]]>Max):
                Max = processes[now_remaining[j]]
                Max_name = now_remaining[j]
            for k in range(j+1, len(now_remaining)):
                if(processes[now_remaining[k]]>processes[now_remaining[j]]):
                    print(now_remaining[j],"sends election message to", now_remaining[k])
            for k in range(j+1, len(now_remaining)):
                if(processes[now_remaining[k]]>processes[now_remaining[j]]):
                    print(now_remaining[k],"sends OK message to", now_remaining[j])
        for i in processes:
            if(processes[i]<processes[Max_name]):
                print(Max_name, "is elected as the coordinator!")
    if(a==2):
        break













# Ring

# number_of_processes = int(input("Enter the number of processes - "))
# processes = []
# for i in range(number_of_processes):
#     id = int(input("Enter the id of process - "))
#     processes.append(id)
# Coordinator = max(processes)
# print("Process",Coordinator, "is the coordinator.")
# while(True):
#     print("1. Initiate a election")
#     print("2. Exit")
#     a = int(input())
#     if(a==1):
#         b = int(input("Enter the id of process to initiate the election from - "))
#         processes.remove(max(processes))
#         c = processes[b-1:]+processes[:b-1]
#         print("Message flow - ", c)
#         Coordinator = max(c)
#         print("Process",Coordinator, "is the coordinator.")
#     if(a==2):
#         break