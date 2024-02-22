Q5. Non decreasing subarray queries
Solved
feature icon
Get your doubts resolved blazing fast with Chat GPT Help
Check Chat GPT
feature icon
Using hints is now penalty free
Use Hint
Problem Description
Given an array A of size N. You will be given M queries to process. Each query will be of the form B[i][0] B[i][1].

If the subarray from B[i][0] to B[i][1] is non decreasing, the output should be 1 else output should be 0.

Return an array of integers answering each query.


Problem Constraints
1 <= N <= 105

1 <= A[i] <= 109

1 <= M <= 105

0 <= B[i][0], B[i][1] <= N-1


Input Format
First argument contains the array A.

Second argument contains B, denoting the queries.


Output Format
Return an array of integers consisting of 0 and 1


Example Input
Input 1:
A = [1, 7, 3, 4, 9]
B = [ 
      [0, 1], 
      [1, 4]
    ]
Input 2:
A = [1, 1, 7, 2, 3]
B = [ 
      [0, 2], 
      [2, 4]
    ]


Example Output
Output 1 :
[1, 0]
Output 2 :
[1, 0]


Example Explanation
Explanation 1 :
Query 1: The subarray in the range [0, 1] is {1, 7} which is non-decreasing. Therefore, ans = 1
Query 2: The subarray in the range [1, 4] is {7, 3, 4, 9} which is not non-decreasing. Therefore, ans = 0
Explanation 1 :
Query 1: The subarray in the range [0, 2] is {1, 1, 7} which is non-decreasing. Therefore, ans = 1
Query 2: The subarray in the range [2, 4] is {7, 2, 3} which is not non-decreasing. Therefore, ans = 0