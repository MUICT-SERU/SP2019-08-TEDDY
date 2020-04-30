def n52():
    seat_A1 = 'Mike Wazowski'
    seat_A2 = 'James P. Sullivan'
    temp = seat_A1
    seat_A1 = seat_A2
    seat_A2 = temp

def n53(numA, numB):
    temp = numA
    numA = numB
    numB = temp

def n54():
    english = 4.0
    math = 3.5
    temp = english
    english = math
    math = temp

def n55(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
