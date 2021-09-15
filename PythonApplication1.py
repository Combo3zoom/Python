def deleteDuplicates(arr):  
    resarr=[arr[0]]
    for i in range(1,len(arr)):
        for j in range(len(resarr)):
            if(resarr[j]==arr[i]):
                check=0
                break
            else:
                check=1  
                
        if check:
            resarr.append(arr[i])
        
    
    arr.clear()
    for i in range(len(resarr)):
        arr.append(resarr[i])

    return 
 
def OutputArr(arr):
    print("Result array: ")
    print(arr)

def InputArr(n,arr):
    print(('Enter '+ str(n) +' Elments : ' ))
    for i in range(n):
       a=float(input())
       arr.append(a)
    return  

while True: 
    try:
        n = int(input('Enter count array: ' ))
        arr=[]
        InputArr(n,arr)
        deleteDuplicates(arr)
        OutputArr(arr)
    except UncorrectValue:
        print("Syntax error, try again")
        continue 
    break
          


