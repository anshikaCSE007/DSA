Problem Description
You are given two integer matrices A(having M X N size) and B(having N X P). You have to multiply matrix A with B and return the resultant matrix. (i.e. return the matrix AB).

Matrix Multiplication 

![alt text](/Arrays/2D-Array/MatrixMultiplication/11464-1.png)

Problem Constraints
1 <= M, N, P <= 100

-100 <= A[i][j], B[i][j] <= 100



Input Format
The first argument given is the 2-D integer matrix A.
The second argument given is the 2-D integer matrix B.



Output Format
Return a 2D integer matrix denoting AB.



Example Input
Input 1:

A = [[1, 2],
     [3, 4]]
B = [[5, 6],
     [7, 8]]
Input 2:

A = [[1, 1]]
B = [[2],
     [3]]


Example Output
Output 1:

 [[19, 22],
  [43, 50]]
Output 2:

 [[5]]


Example Explanation
Explanation 1:

 
Explanation 2:

 [[1, 1]].[[2], [3]] = [[1 * 2 + 1 * 3]] = [[5]]

