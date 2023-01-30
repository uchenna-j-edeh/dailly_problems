"""Good morning! Here's your coding interview problem for today.

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?

"""

def kth_pascal_triangle(k):
    i = 1
    while i <= k:
        if i == 1:
            n = '11'
        else:
            for j in len(n):
                current = int(n[i])
