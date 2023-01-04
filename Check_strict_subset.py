# Enter your code here. Read input from STDIN. Print output to STDOUT
set_A = list(map(int, input().split()))
set_no = int(input())
sets = []
answer = True

for index in range(set_no):
    sett = list(map(int, input().split()))
    sets.append(sett)

for i in sets:
    if len(set_A) <= len(i):
        answer = False
        
for i in sets:
    for j in i:
        if j not in set_A:
            answer = False
            
print(answer)
