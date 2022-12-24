# Enter your code here. Read input from STDIN. Print output to STDOUT
pilling_no = int(input())
for i in range(pilling_no):
    cube_no = int(input())
    cubes = list(map(int, input().split(" ")))
    new = []
    yes = 1
    i = 0
    j = -1
    k = 0
    while k < cube_no:
        if len(new) > 0:
            if cubes[i] >= cubes[j]:
                if new[-1] >= cubes[i]:
                    new.append(cubes[i])
                    i += 1
                else:
                    yes = 0
                    break
            elif cubes[i] < cubes[j]:
                if new[-1] >= cubes[j]:
                    new.append(cubes[j])
                    j -= 1
                else:
                    yes = 0
                    break
        else:
            if cubes[i] >= cubes[j]:
                new.append(cubes[i])
                i+=1
            else:
                new.append(cubes[j])
                j-=1
        k += 1
                
    if yes == 0:
        print("No")
    else:
        print("Yes")
