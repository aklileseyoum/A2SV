# Enter your code here. Read input from STDIN. Print output to STDOUT
#nums = list(map(int, input().split(" ")))
leng = list(map(int, input().split(" ")))
listt = list(map(int, input().split(" ")))
A = set(map(int, input().split(" ")))
B = set(map(int, input().split(" ")))

happy = 0
for i in listt:
    if i in A:
        happy += 1
    elif i in B:
        happy -= 1

print(happy)
