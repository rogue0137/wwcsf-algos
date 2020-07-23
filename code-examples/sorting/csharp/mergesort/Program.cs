/*
912. Sort an Array
Medium
Given an array of integers nums, sort the array in ascending order.
Leetcode link
https://leetcode.com/problems/sort-an-array/
*/

using System;

namespace mergesort
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Sorted Array with merge sort");

            int[] a = new int[8]{2,4,1,6,8,5,3,7};   
            sortArray(a);           
        }

        static int[] sortArray(int[] a)
        {            
            // split the array only if the array has 2 or more elements
            if (a.Length < 2)
                return a;

            int[] l = new int[a.Length/2];
            int[] r = new int[a.Length - a.Length/2];

            for (int i = 0; i < l.Length; i++)
            {
                l[i] = a[i];                   
            }
            for (int j = 0; j < r.Length; j++)
            {
                r[j] = a[j + l.Length];
            }  
            sortArray(l);
            sortArray(r);
            mergeArrays(l,r,a);
            return a;
        }

        static int[] mergeArrays(int[] left, int[] right, int[] a)
        {            
           
          // mergeing the arrays that are already sorted into a
          // picked the smallest from left and right and put it into a

           int k = 0;  // the position for the insertion point in a
           int i = 0;  // the position for the extraction of an element in left
           int j = 0; // the position for extracting an element in right

           while (i < left.Length && j < right.Length)
           {
               if (left[i] <= right[j])
               {
                   a[k] = left[i];                  
                   i++;                  
               }
               else
               {
                   a[k] = right[j];                
                   j++;
               }
            k++;             
           }
           // check if there are some left elements in any of the arrays left or right
           while(i < left.Length)
           {
               a[k] = left[i];
               k++;
               i++;
           }

           while(j < right.Length)
           {
               a[k] = right[j];
               k++;
               j++;
           }

           return a;
        }
        
    }
}
