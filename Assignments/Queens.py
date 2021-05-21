###
# Michael Buffone
# May 19th, 2021
# COSC4427 Assignment 1
#
# This program will explore the N-Queens problem where no two queens attack each other.
# 
###

# Given an integer 1 <= N <= 10
class Puzzle:
    n = 0
    board = [[]]
    
    # Constructor to create board based on given size
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        
    # Method to find a safe place
    def solvePuzzle(self, column):
        if column >= self.n:
            return True
        
        for i in range(self.n):
            if self.isSafe(i, column):
                self.placeQueen(i, column)
                
            if self.solvePuzzle(column + 1) == True:
                return True
            
            self.removeQueen(i, column)
            
        return False
    
    # Method to check if a position is safe
    def isSafe(self, row, column):
        
        # Check all of the positions horizontally and vertically to see if there's a queen
        for i in range(self.n):
            if(self.board[row][i] == 1 or self.board[i][column] == 1):
                return False
            
        startingPos = min(row, column) - 1
        
        # Check the left diagonals (zip function combines row and column together)
        for i,j in zip(range(row, -1, -1), range(column, -1, -1)):
            if(self.board[i][j] == 1):
                return False
            
        for i,j in zip(range(row, self.n, 1), range(column, -1, -1)):
            if(self.board[i][j] == 1):
                return False
            
        return True
            
    # Method to place a queen on the board
    def placeQueen(self, x, y):
        self.board[x][y] = 1
    
    # Method to remove a queen on the board
    def removeQueen(self, x, y):
        self.board[x][y] = 0
        
    # Method to print the board
    def displayBoard(self):
        print("Board of size N = ", self.n, ":", sep = "")
        for i in range(self.n):
                for j in range(self.n):
                    print(self.board[i][j], " ", end="")
                print()
            
def main():
    print("-----")
    # Collect the size from the user and create the puzzle board
    puzzle1 = Puzzle(int(input("Enter a board of size N: ")))
    puzzle1.displayBoard()
    
    if puzzle1.solvePuzzle(0):
        print("Solution found!")
        puzzle1.displayBoard()
    
    
    print("-----")
    
if __name__ == "__main__":
    main()