from collections import defaultdict

class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        if (len(board) != 9) or (len(board[0]) != 9) :
            return False
        def ifvalid(data):
            dict = defaultdict(int)
            for numchar in data:
                dict[numchar] += 1
            for num, amount in dict.items():
                if(num != '.' and amount >1):
                    return False
            return True
            
        #check rows
        for row in board:
            if (not ifvalid(list(row))):
                return False
        
        #check columns
        for i in range(0,9):
            column = []
            for j in range(0,9):
                column.append(board[j][i])
            if (not ifvalid(list(column))):
                return False
        
        #check squares
        for rownum in range(0,3):
            for colnum in range(0,3):
                box = []
                
                for x in range(0,3):
                    for y in range(0,3):
                        box.append(board[rownum * 3 +x][colnum *3 +y])
                if (not ifvalid(list(box))):
                    return False
        return True

S = Solution()
print S.isValidSudoku(["..4...63.",".........","5......9.","...56....","4.3.....1","...7.....","...5.....",".........","........."])