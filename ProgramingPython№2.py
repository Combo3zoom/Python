def InputArray(array,size):
    for i in range(size):
      array.append([])
      for j in range(size):
          array[i] += [float(input())]
    print()
    return
            
def OutputArray(array,size):
    for i in range(size):
        print(array[i])
    print()
    return


def MaxElementsInNegativeDiagonal(array,size):
    currentElement=array[0][0]
    listMinElements=[]
    for i in range(size):
        for j in range(size):
            if(i==j):
                currentElement=array[i][j]
                if(currentElement<0):
                    currentMin= array[j][0]
                    for k in range(size):
                        if(currentMin>array[j][k]):
                            currentMin=array[j][k]
                    listMinElements.append(currentMin)
    max=listMinElements[0]
    for i in range(len(listMinElements)):      
        if(max<listMinElements[i]):
            max=listMinElements[i]
    print("Maximal elements: ",max)
    return

while True:
    try:
        array = []
        size=int(input("Enter array order: "))
        while(size<=0):
            size=int(input("Enter array order more 0: "))
        InputArray(array,size)
        OutputArray(array,size)
        MaxElementsInNegativeDiagonal(array,size)
    except ValueError:
        print("Syntax error, try again ")
        continue
    break 




