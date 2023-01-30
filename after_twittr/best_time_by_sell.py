"""
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.

strategy: construct aux array of low high. eventually sort to evaluate unique low followed by highest high point. that is buy low sell high
"""

def buy_low_sell_high(arr):
    high_low = []
    for i in range(len(arr)):
        if i+1 < len(arr):
            if arr[i] > arr[i+1]:
                high_low.append((i, 'H'))
            if arr[i] < arr[i+1]:
                high_low.append((i, 'L'))

    j = 0
    while j < len(high_low) - 1:
        _, h_l_1 = high_low[i]
        _, h_l_2 = high_low[i+2]
        if h_l_1 == 'H' and h_l_2 == 'H':
            del high_low[i]

        if h_l_1 == 'L' and h_l_2 == 'L':
            del high_low(i)

    for k in range(len(arr)):
        if i+1 < len(high_low):
            






