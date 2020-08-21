def is_dip(k):
    high = 0
    for n in range(k, len(prices)):
        if n+1 < len(prices) and prices[n] < prices[n+1]:
           high = n + 1
        else:
            break
    return high

