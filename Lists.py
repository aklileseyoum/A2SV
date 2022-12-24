if __name__ == '__main__':
    N = int(input())
    
    new_list = []
    for i in range(N):
        command = list(input().split(" "))
        if command[0] == "insert":
            new_list.insert(int(command[1]), int(command[2]))
        elif command[0] == "print":
            print(new_list)
        elif command[0] == "remove":
            if int(command[1]) in new_list:
                new_list.remove(int(command[1]))
        elif command[0] == "append":
            new_list.append(int(command[1]))
        elif command[0] == "sort":
            new_list.sort()
        elif command[0] == "pop":
            if len(new_list) > 0:
                new_list.pop()
        elif command[0] == "reverse":
            new_list.reverse()
