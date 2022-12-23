if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input()) 
        records.append([name, score])
        
    if len(records) != 1:
        records.sort(key = lambda x: x[1])
        
        score2 = records[1][1]
        if score2 == records[0][1]:
            i = 2
            while score2 == records[i][1]:
                i += 1
            score2 = records[i][1]
        names=[]
        for i in records:
            if i[1] == score2:
                names.append(i[0])
        
        names.sort()
        for i in names:
            print(i)
        
    else:
        print(records[0][0])
