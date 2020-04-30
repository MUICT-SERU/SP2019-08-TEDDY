def i47():
    seat_A1 = 'Mike Wazowski'
    seat_A2 = 'James Sullivan'
    (seat_A1, seat_A2) = (seat_A2, seat_A1)

def i48(var_A, var_B):
    (var_A, var_B) = (var_B, var_A)

def i49():
    english = 4.0
    math = 3.5
    (english, math) = (math, english)

def i50(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                (arr[j], arr[j+1]) = (arr[j+1], arr[j])

