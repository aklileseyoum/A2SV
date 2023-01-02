    position = input()
    positions = []
    for i in position:
        positions.append(i)
    column = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    current_row = int(positions[1])
    current_column = positions[0]
    moves = 0
    if (chr(ord(current_column)-1)) in column:
        if current_row > 1 and current_row < 8:
            moves += 3
        elif current_row == 1 or current_row == 8:
            moves += 2
    if (chr(ord(current_column)+1)) in column:
        if current_row > 1 and current_row < 8:
            moves += 3
        elif current_row == 1 or current_row == 8:
            moves += 2
    if current_row > 1 and current_row < 8:
        moves += 2
    elif current_row == 1 or current_row == 8:
        moves += 1
        
    print(moves)
