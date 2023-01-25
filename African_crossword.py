    from collections import defaultdict
    size = list(map(int, input().split()))
    crossword = []
    for row in range(size[0]):
        word = input()
        crossword.append(word)
        
    answer = ""
    for row in range(size[0]):
        for col in range(size[1]):
            letter = crossword[row][col]
            count = crossword[row].count(letter)
            yes = 1
            for i in range(size[0]):
                if i != row:
                    if letter == crossword[i][col]:
                        yes = 0
                        
            if yes == 1 and count == 1:
                answer += letter
                
    print(answer)
