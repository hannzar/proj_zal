# proj_zal

1.  Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string.
    Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Function Description:
Complete the function sherlockAndAnagrams in the editor below.
sherlockAndAnagrams has the following parameter(s):
string s- a string

Returns:
int- the number of unordered anagrammatic pairs of substrings in s

Constraints:
2 <= length of s <= 100,
s contains only lowercase letters in the range ascii[a-z].

 

2. Consider a matrix where each cell contains either a 0 or a 1. Any cell containing a 1 is called a filled cell. Two cells are said to be connected if they are adjacent to each other horizontally, vertically, or diagonally. In the following grid, all cells marked X are connected to the cell marked Y.

XXX
XYX 
XXX 

If one or more filled cells are also connected, they form a region. Note that each cell in a region is connected to zero or more cells in the region but is not necessarily directly connected to all the other cells in the region.
Given an  matrix, find and print the number of cells in the largest region in the matrix. Note that there may be more than one region in the matrix.

Function Description:
Complete the connectedCell function in the editor below.
connectedCell has the following parameter(s):
int matrix[n][m]

Returns:
int- the area of the largest region

Constraints:
0 < n, m < 10
