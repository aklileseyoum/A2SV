# Enter your code here. Read input from STDIN. Print output to STDOUT
num = int(input())
inp = []
for i in range(num):
    a = input()
    inp.append(a)
ans = {}
for i in inp:
    if i not in ans:
        ans[i] = 1
    else:
        j = ans[i]
        ans[i] = j+1

print(len(ans))
for i in ans:
    print(ans[i],end=" ")
