# COSC4427A Midterm Question 2
# Michael Buffone

def findSubarray(userArray, d):
    if sum(userArray) % d == 0:
        return 0
    
    # Generate all of the subarrays
    subarrayList = []
    for i in range(len(userArray)):
        for j in range(len(userArray)):
            temp = userArray[i:j+1]
            if temp != []:
                subarrayList.append(temp)  
    
    # Sort based on length
    subarrayList.sort()
    subarrayList.sort(key = len)
    
    # Find the subarray combination and remove it from a temp list
    for subarray in subarrayList:
        userCopy = userArray.copy()
       
        for j in range(len(subarray)):
            userCopy.remove(subarray[j])
            
        if len(userCopy) == 0:
            return -1

        if sum(userCopy) % d == 0:
            return subarray
        
    return -1
            
def driver():
    userArr = input("Enter arr: ")
    userDInput = input("Enter d: ")
    userArr = userArr.replace("[", "")
    userArr = userArr.replace("]", "")
    userArr = userArr.replace(",", "")
    userArr = userArr.split()
    for i in range(len(userArr)):
        userArr[i] = int(userArr[i])
    
    print("Output:", findSubarray(userArr, (int)(userDInput)))
        
for i in range(4):
    driver()