/*
37. Sudoku Solver
Hard

Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1-9 must occur exactly once in each row.
Each of the digits 1-9 must occur exactly once in each column.
Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Leetcode link

https://leetcode.com/problems/sudoku-solver/
*/

using System;

class Solution
{
     public static void SolveSudoku(char[][] board) {               
      CompleteBoard(board);    
    }            

    public static bool CompleteBoard(char[][] board)
    {
        int row = -1;
        int col = -1;
        
        var isComplete = true; 
        
        // look at complete rows or cols
        for (int i = 0; i < board[0].Length; i++)
        {
            for (int j = 0; j < board[0].Length; j++)
            {
                if (board[i][j] == '.')
                {
                    row = i;
                    col = j;
                    isComplete = false;
                    break;
                }
            }
            if (!isComplete)
                break;
        }
        
        if (isComplete)
        {   
            return true;

        }
        
        // look for a number to fill the empty cell        
      for (char ch = '1'; ch <= '9'; ch++)        
        {
            if (IsValid(board, row, col, ch))
            {
                board[row][col] = ch;
                // PrintBoard(board);
                if (CompleteBoard(board))
                   return true;               
                else
                {
                    board[row][col] = '.';                    
                }
            }
        }
        
      return false;
    }
    
    public static bool IsValid(char[][] board, int row, int col, char k)
    {        
        //row check
        for (int i = 0; i < 9; i++)
        {           
            if (board[row][i] == k)
                return false;
        }
        
        //col check
        for (int i = 0; i < 9; i++)
        {
            if (board[i][col] == k)
                return false;
        }
        
        // 3x3 board check
        int rowStart = row - row % 3;
        int colStart = col - col % 3;
        
        for (int r = rowStart; r < rowStart + 3; r++)
        {
            for (int c = colStart; c < colStart + 3; c++)
            {
                if (board[r][c] == k)
                    return false;
            }
        }
        
        return true;
    }

    public static void PrintBoard(char[][] board)
    {
        for (int i = 0; i < 9; i++)
        {
          var chars = board[i];
          Console.Write("| " );
          foreach(char c in chars) 
              Console.Write(" " + c); 
          Console.WriteLine(" |" );                
      }
      Console.WriteLine("_____________");
    }

    static void Main(string[] args)
    {
      char[][] board = new char[9][]{
        new char[9] {'5','3','.','.','7','.','.','.','.'},
        new char[9] {'6','.','.','1','9','5','.','.','.'},
       new char[9] {'.','9','8','.','.','.','.','6','.'},
       new char[9] {'8','.','.','.','6','.','.','.','3'},
       new char[9] {'4','.','.','8','.','3','.','.','1'},
       new char[9] {'7','.','.','.','2','.','.','.','6'},
       new char[9] {'.','6','.','.','.','.','2','8','.'},
       new char[9] {'.','.','.','4','1','9','.','.','5'},
       new char[9] {'.','.','.','.','8','.','.','7','9'}};

      
      Console.WriteLine("=== Board ===");
      PrintBoard(board);
      SolveSudoku(board);
      Console.WriteLine("=== Solved sudoku ===");
      PrintBoard(board);
      
    }
}

