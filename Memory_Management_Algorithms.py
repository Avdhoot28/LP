blockSize = [200, 30, 700, 50]
processSize = [20, 200, 500, 190]
m = len(blockSize)
n = len(processSize)


print("Best Fit - ")

def bestFit(blockSize, m, processSize, n):
	
	allocation = [-1] * n


	for i in range(n):
		
		bestIdx = -1
		for j in range(m):
			if blockSize[j] >= processSize[i]:
				if bestIdx == -1:
					bestIdx = j
				elif blockSize[bestIdx] > blockSize[j]:
					bestIdx = j

		if bestIdx != -1:
			
			allocation[i] = bestIdx

			blockSize[bestIdx] -= processSize[i]
			
	for i in range(n):
	    print(processSize[i], " ", allocation[i]+1)

    



bestFit(blockSize, m, processSize, n)



blockSize = [200, 30, 700, 50]
processSize = [20, 200, 500, 190]
m = len(blockSize)
n = len(processSize)

print()
print("First Fit - ")

def firstFit(blockSize, m, processSize, n):
    
    allocation = [-1] * n
  
    for i in range(n):
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                  
                allocation[i] = j 
  
                blockSize[j] -= processSize[i] 
  
                break
  
    for i in range(n):
        print(processSize[i], end = "    ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


firstFit(blockSize, m, processSize, n)


blockSize = [200, 30, 700, 50]
processSize = [20, 200, 500, 190, 999999]
m = len(blockSize)
n = len(processSize)

print()
print("Next Fit - ")

def NextFit(blockSize, m, processSize, n):
    allocation = [-1] * n
    j = 0
    while j < m:
        for i in range(n):
            if blockSize[j] >= processSize[i]:
 
                allocation[i] = j
 
                blockSize[j] -= processSize[i]

                if(blockSize[j] < processSize[i+1]):
                    j = j+1
            if(j >= m):
                break

    for i in range(n):
        print(processSize[i], end = "    ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")



NextFit(blockSize, m, processSize, n)


blockSize = [100, 500, 200, 300, 600]
processSize = [212, 417, 112, 426]
m = len(blockSize)
n = len(processSize)

print()
print("Worst Fit - ")

def worstFit(blockSize, m, processSize, n):
     
    allocation = [-1] * n
     
    for i in range(n):
         
        wstIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if wstIdx == -1:
                    wstIdx = j
                elif blockSize[wstIdx] < blockSize[j]:
                    wstIdx = j
 
        if wstIdx != -1:
             
            allocation[i] = wstIdx
 
            blockSize[wstIdx] -= processSize[i]
 
    for i in range(n):
        print(processSize[i], end = "    ")
        if allocation[i] != -1:
            print(allocation[i] + 1)
        else:
            print("Not Allocated")


worstFit(blockSize, m, processSize, n)