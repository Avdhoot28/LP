

P1 = {}
P2 = {}
P1_count = 1
P2_count = 1
count = 0

while(True):
    print("1. add a event to P1")
    print("2. add a event to P2")
    print("3. send a message from P1 to P2")
    print("4. send a message from P2 to P1")
    a = int(input())
    if(a==1):
        P1[chr(65+count)] = P1_count
        P1_count+=1
        count+=1
        print(P1)
    elif(a==2):
        P2[chr(65+count)] = P2_count
        P2_count+=1
        count+=1
        print(P2)
    elif(a==3):
        P2[chr(65+count)] = max(P2_count,P1_count)
        P2_count+=1
        count+=1
        print(P2)
    elif(a==4):
        P1[chr(65+count)] = max(P1_count,P2_count)
        P1_count+=1
        count+=1
        print(P1)