###
# Michael Buffone
# May 19th, 2021
# COSC4427 code Assignment 1
#
# This program will explore the N-Queens problem where no two queens attack each other.
# 
###

# Given an integer 1 <= N <= 10 which represents the board size
class Puzzle:
    n = 0
    solutionCount = 0
    board = [[]]
    
    # Constructor to create board based on given size
    def __init__(self, n):
        self.n = n
        self.board = [[0 for i in range(n)] for j in range(n)]
        
    # Driver method to find a spot on the board to place queens, starting from 0 in main
    def solvePuzzle(self, row):
        
        # We have found a solution (base case for the problem)
        if row == self.n:
            self.solutionCount += 1
            self.displayBoard()
            return
        
        # Go to the next row and place a queen when it is safe    
        for i in range(self.n):
            if self.isSafe(row, i):
                self.placeQueen(row, i)
                self.solvePuzzle(row + 1)
                # Undo the move
                self.removeQueen(row, i)
    
    # Method to check if a position is safe
    def isSafe(self, row, column):
        
        # Check all of the positions horizontally
        for i in range(row):
            if(self.board[i][column] == 1):
                return False
        
        # Check all of the positions vertically    
        for i in range(column):
            if(self.board[row][i] == 1):
                return False
                    
        # Check all of the positions within the first diagonal
        for i,j in zip(range(row, -1, -1), range(column, -1, -1)):
            if(self.board[i][j] == 1):
                return False
                    
        # Check all of the positions within the second diagonal 
        for i,j in zip(range(row, -1, -1), range(column, self.n, 1)):
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
    userNum = input("Enter a board of size N: ")
    puzzle = Puzzle(int(userNum))
    puzzle.displayBoard()
    
    # Solve the puzzle
    print("\nSolving...")
    puzzle.solvePuzzle(0)
    print(puzzle.solutionCount, "solutions found when N =", userNum)
    
    print("-----")
    
if __name__ == "__main__":
    main()