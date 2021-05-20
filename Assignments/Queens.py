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
    #def findASafePlace(self):
    
    # Method to check if a position is safe
    def isSafe(self, row, column):
        
        # Check all of the positions horizontally and vertically to see if there's a queen
        for i in range(self.n):
            if(self.board[row][i] == 1 or self.board[i][column] == 1):
                return False
            
        startingPos = min(row, column) - 1
        # Check the diagonals
        #for i in range(startingPos, )
        
    
    # Method to place a queen on the board
    #def placeQueen(self):
    
    # Method to remove a queen on the board
    #def removeQueen(self):
        
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
    print("-----")
    
if __name__ == "__main__":
    main()