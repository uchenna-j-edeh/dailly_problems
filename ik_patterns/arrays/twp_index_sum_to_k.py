def solution(a, k):
    count = 0
    for i in range(len(a)):
        for j in range(i+1, len(a)):
            sum_a = a[i] + a[j]
            if sum_a % k == 0:
                count += 1

    return count

print(solution([1,2,3,4,5], 3))