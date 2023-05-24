

Given a sorted array of integers A (0-indexed) of size N, find the starting and the ending position of a given integer B in array A.

Return an array of size 2, such that 
          First element = Starting position of B in A
          Second element = Ending position of B in A.
If B is not found in A, return [-1, -1].

Note : 
Your algorithm's runtime complexity must be in the order of O(log n).


Problem Constraints
1 <= N <= 106
1 <= A[i], B <= 109


Input Format
The first argument given is the integer array A.
The second argument given is the integer B.


Output Format
Return the starting and ending positions of B in A as a 2-element array. If B is not found in A, return [-1, -1].


Example Input
Input 1:

 A = [5, 7, 7, 8, 8, 10]
 B = 8
Input 2:

 A = [5, 17, 100, 111]
 B = 3


Example Output
Output 1:

 [3, 4]
Output 2:

 [-1, -1]