if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = set(arr)
    arr = list(arr)
    arr.sort()
    if len(arr) >= 2:
        print(arr[-2])
    else:
        print(arr[-1])
