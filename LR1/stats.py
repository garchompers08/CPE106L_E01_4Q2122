#median function
def median(num):
    num.sort()
    n = len(num)
    mid = int(n / 2);
    if(n % 2 == 1):
        return num[mid]
    else:
        return (num[mid] + num[mid + 1]) / 2

 #mode function 
def mode(num):
    modeNum = max(set(num), key = num.count)
    return modeNum

#mean function 
def mean(num):
    n = len(num)
    sumOfNum = 0
    for i in num:
        sumOfNum = sumOfNum + i;
    return sumOfNum / n

num = [8,3,10,2,9,1,7,6,4,5]

print(median(num))
print(mode(num))
print(mean(num))
