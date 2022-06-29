
 
def first(arr, low, high, x, n) :
    if (high >= low) :
        mid = low + (high - low) // 2;  # (low + high)/2;
        if ((mid == 0 or x > arr[mid-1]) and arr[mid] == x) :
            return mid
        if (x > arr[mid]) :
            return first(arr, (mid + 1), high, x, n)
        return first(arr, low, (mid -1), x, n)
         
    return -1

def sortAccording(A1, A2, m, n) :
   

    visited = [0] * m
     
    for i in range(0, m) :
        temp[i] = A1[i]
        visited[i] = 0
  
    temp.sort()
    
    ind = 0   
    for i in range(0, n) :
         
        f = first(temp, 0, m-1, A2[i], m)
  
        f (f == -1) :
            continue
  
        j = f
        while (j<m and temp[j]== A2[i]) :
            A1[ind] = temp[j];
            ind = ind + 1
            visited[j] = 1
            j = j + 1
    
    for i in range(0, m) :
        if (visited[i] == 0) :
            A1[ind] = temp[i]
            ind = ind + 1
             
def printArray(arr, n) :
    for i in range(0, n) :
        print(arr[i], end = " ")
    print("")
     

A1 = [2, 1, 2, 5, 7, 1, 9, 3, 6, 8, 8]
A2 = [2, 1, 8, 3]
m = len(A1)
n = len(A2)
print("Sorted array is ")
sortAccording(A1, A2, m, n)
printArray(A1, m)
