/*
54. Spiral Matrix
Medium
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
Leetcode link https://leetcode.com/problems/spiral-matrix/
The following code has two implementations: SpiralMatrixToArray and SpiralMatrixToConsole
*/

using System;

namespace spiralmatriz
{
    class Program
    {
        static void Main(string[] args)
        {
            // Test 1
            // int[,] a = new int [,] {{2,4,6,8}, {5,9,12,16}, {2,11,5,9}, {3,2,1,8}};
            
            // Test 2
            int[,] a = new int[,] { { 1 }, { 2 } };
            var result = SpiralMatrixToArray(a);

            for (int i = 0; i < result.Length; i++)
            {
                Console.WriteLine(result[i]);
            }
        }

        static int[] SpiralMatrixToArray(int[,] inputMatrix)
        {
            if (inputMatrix.GetLength(1) == 0 && inputMatrix.GetLength(0) == 0)
                return new int[0];

            var iterator = 0;
            int row = 0;
            int colright = inputMatrix.GetLength(1) - 1;
            int colLeft = 0;
            var l = inputMatrix.GetLength(1) * inputMatrix.GetLength(0);
            var spiralCopy = new int[l];
            var indexSpiral = 0;
            var bottom = inputMatrix.GetLength(0) - 1; // number of rows

            while (row < bottom && colLeft < colright)
            {
                if (iterator == 0)
                {
                    // top left to top right
                    for (int i = colLeft; i <= colright; i++)
                    {
                        spiralCopy[indexSpiral++] = inputMatrix[row, i];
                    }
                    row++;
                    iterator = 1;
                }

                if (iterator == 1)
                {
                    // right top to the bottom right
                    for (int i = row; i <= bottom; i++)
                    {
                        spiralCopy[indexSpiral++] = inputMatrix[i, colright];
                    }
                    colright--;
                    iterator = 2;
                }

                if (iterator == 2)
                {
                    // bottom right to bottom left
                    for (int i = colright; i >= colLeft; i--)
                    {
                        spiralCopy[indexSpiral++] = inputMatrix[bottom, i];
                    }
                    bottom--;
                    iterator = 3;
                }

                if (iterator == 3)
                {
                    // bottom left to top right
                    for (int i = bottom; i >= row; i--)
                    {
                        spiralCopy[indexSpiral++] = inputMatrix[i, colLeft];
                    }
                    colLeft++;
                    iterator = 0;
                }
            }
            return spiralCopy;
        }

        static void SpiralMatrixToConsole(int[,] a)
        {
            int rows = a.GetLength(0);
            int columns = a.GetLength(1);

            int top = 0;
            int bottom = rows - 1;
            int left = 0;
            int right = columns - 1;
            int direction = 0; // 0 left to righ, 1 top to bottom, 2 right to left, 3 bottom to top

            while (bottom >= top && right >= left)
            {
                if (direction == 0)
                {
                    for (int i = left; i <= right; i++)
                    {
                        Console.Write(a[top, i]);
                    }
                    top++;
                    direction = 1;
                }
                if (direction == 1)
                {
                    for (int i = top; i <= bottom; i++)
                    {
                        Console.Write(a[i, right]);
                    }
                    right--;
                    direction = 2;
                }
                if (direction == 2)
                {
                    for (int i = right; i >= left; i--)
                    {
                        Console.Write(a[bottom, i]);
                    }
                    bottom--;
                    direction = 3;
                }
                if (direction == 3)
                {
                    for (int i = bottom; i >= top; i--)
                    {
                        Console.Write(a[i, left]);
                    }
                    left++;
                    direction = 0;
                }
            }
        }
    }
}
