# Enter your code here. Read input from STDIN. Print output to STDOUT
no = list(map(int, input().split(" ")))
marks = [[0]*no[0]]*no[1]
for i in range(no[1]):
    marks[i] = list(map(float, input().split()))


for i in range(no[0]):
    summ = 0
    for j in range(no[1]):
        summ += marks[j][i]
    average = summ / no[1]
    print(average)
        
