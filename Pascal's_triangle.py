class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        array = [0] * (rowIndex + 1)
        memo ={}

        def getCol(row, col):
            if col == 0 or col == row or row == 0 or row == 1:
                return 1

            if (row, col) in memo:
                return memo[(row, col)]
                
            memo[(row, col)] = getCol(row - 1, col - 1) + getCol(row - 1, col)
            return memo[(row, col)]
            
        length = (rowIndex // 2) + 1
        for col in range(length):
            array[col] = getCol(rowIndex, col) 
        
        array = array[:length]
        if rowIndex % 2 == 0:
            new = array[:len(array)-1][::-1]  
        else:
            new = array[::-1]
        array.extend(new)

        return array
