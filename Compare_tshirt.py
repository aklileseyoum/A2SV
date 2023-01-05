    num = int(input())
    X_L = 1
    X_S = -1
    S = 0
    M = 1
    L = 2
    for i in range(num):
        sizes = list(input().split())
        first_size = sizes[0]
        second_size = sizes[1]
        if first_size == second_size:
            print("=")
        else:
            X_first = first_size.count('X')
            X_second = second_size.count('X')
            value_first = 0
            value_second = 0
            if 'S' in first_size:
                value_first += X_first * X_S
            elif 'L' in first_size:
                value_first += X_first * X_L
                value_first += L
            else:
                value_first += M
                
            if 'S' in second_size:
                value_second += X_second * X_S
            elif 'L' in second_size:
                value_second += X_second * X_L
                value_second += L
            else:
                value_second += M
                
            if value_first > value_second :
                print(">")
            elif value_first < value_second:
                print("<")
