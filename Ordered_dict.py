# Enter your code here. Read input from STDIN. Print output to STDOUT
item_no = int(input())
itemss = {}
for i in range(item_no):
    item_info = list(input().split(" "))
    name = ""
    k = 0
    while k+1 < len(item_info):
        name += item_info[k]
        name += " "
        k += 1
        
    if name in itemss:
        itemss[name] += int(item_info[-1])
    else:
        itemss[name] = int(item_info[-1])
    
for i in itemss:
    print(i,end="")
    print(itemss[i])
