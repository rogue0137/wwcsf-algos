/* 
130. Surrounded Regions
Medium

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.

A region is captured by flipping all 'O's into 'X's in that surrounded region.

Leetcode link 
https://leetcode.com/problems/surrounded-regions/

Solution

1. Traverse the matrix and change all the 'O' by '-'
2. Check the edges and it's adjacent cell's to be 'O' as originally
3. The rest of the '-' are the cells that can be flipped to 'X'

*/

using System;

namespace surrounded_regions
{
    class Program
    {
        static void Main(string[] args)
        {

            int[,] matrix = new int[5,4];
            Console.WriteLine(matrix.GetLength(0) + " " + matrix.GetLength(1));
            

            return;

            // board 6 x 6
            char[][] board =
                new char[6][]
                {
                    new char[6] { 'X', 'O', 'X', 'X', 'X', 'X' },
                    new char[6] { 'X', 'O', 'X', 'X', 'O', 'X' },
                    new char[6] { 'X', 'X', 'X', 'O', 'O', 'X' },
                    new char[6] { 'O', 'X', 'X', 'X', 'X', 'X' },
                    new char[6] { 'X', 'X', 'X', 'O', 'X', 'O' },
                    new char[6] { 'O', 'O', 'X', 'O', 'O', 'O' }
                };

            Console.WriteLine("======= input =====");
            PrintBoard (board);

            ReplaceSurrounded (board);

            PrintBoard (board);

            Console.WriteLine("======= output =====");

             PrintBoard (board);
        }

        public static void ReplaceSurrounded(char[][] board)
        {
            // Step 1 - Replace all O by -
            for (int i = 0; i < board.Length; i++)
            {
                for (int j = 0; j < board[0].Length; j++)
                {
                    if (board[i][j] == 'O')
                    {
                        board[i][j] = '-';
                    }
                }
            }

            // Step 2 - check all edges
            // top side
            for (int i = 0; i < board[0].Length; i++)
            {
                if (board[0][i] == '-') DFSHelper(board, 0, i, '-', 'O');
            }
            // bottom side
            for (int i = 0; i < board[0].Length; i++)
            {
                if (board[board.Length - 1][i] == '-') DFSHelper(board, board.Length - 1, i, '-', 'O');
            }

            //left side
            for (int i = 0; i < board.Length; i++)
            {
                if (board[i][0] == '-') DFSHelper(board, i, 0, '-', 'O');
            }

            //right side
            for (int i = 0; i < board.Length; i++)
            {
                if (board[i][board[0].Length - 1] == '-') DFSHelper(board, i, board[0].Length - 1, '-', 'O');
            }
         
            // step 3 replace the remaining '-' by 'X
            for (int i = 0; i < board.Length; i++)
            {
                for (int j = 0; j < board[0].Length; j++)
                {
                    if (board[i][j] == '-')
                    {
                        board[i][j] = 'X';
                    }
                }
            }

        }

        private static void DFSHelper(
            char[][] board,
            int row,
            int col,
            char prevChar,
            char newChar
        )
        {
            // base case
            if (
                row < 0 ||
                row >= board.Length ||
                col < 0 ||
                col >= board[0].Length
            ) return;


            if (board[row][col] != prevChar)
              return;
              
            board[row][col] = newChar;

            //north
            DFSHelper(board, row - 1, col, prevChar, newChar);

            //south
            DFSHelper(board, row + 1, col, prevChar, newChar);

            //east
            DFSHelper(board, row, col - 1, prevChar, newChar);

            //west
            DFSHelper(board, row, col + 1, prevChar, newChar);
        }

        public static void PrintBoard(char[][] board)
        {
            for (int i = 0; i < board.Length; i++)
            {
                var chars = board[i];
                Console.Write("| ");
                foreach (char c in chars) Console.Write(" " + c);
                Console.WriteLine(" |");
            }
            Console.WriteLine("_____________");
        }
    }
}
