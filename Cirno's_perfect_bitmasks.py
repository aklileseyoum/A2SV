testcases = int(input())
for _ in range(testcases):
    x = int(input())
    if x == 1:
        print(3)
    elif x % 2 == 1:
        print(1)
    else:
        ones = bin(x).count('1')
        if ones == 1:
            print(x + 1)
        else:
            idx = 0
            for i in range(x):
                if x & (1 << i) != 0:
                    idx = i
                    break
            x &= (1 << idx)
            print(x)