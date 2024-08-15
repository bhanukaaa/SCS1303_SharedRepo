def partition(array):
    sublistA = []
    sublistB = []

    n = len(array)
    for i in range(n - 1): # Bubble Sort
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]

    for i in range(n):
        if i % 2 == 0:
            sublistA.append(array[i])
        else:
            sublistB.append(array[i])
    
    print(sublistA)
    print(sublistB)

    return sublistA, sublistB


partition([3,43,633,5,2,5,7,5,4,2,42,45,56,2,5,6,3,35,6,23,41,43,34,6])

