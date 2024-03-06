# 최소값
def MinValue(A):
    Temp = 0
    for i in A :
        if Temp == 0 or i < Temp :
            Temp = i
    print(Temp)
 
# 최대값
def MaxValue(A):
    Temp = 0
    for i in A :
        if Temp == 0 or i > Temp :
            Temp = i
    print(Temp)