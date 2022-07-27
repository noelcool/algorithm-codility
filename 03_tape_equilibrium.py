def solution(A):
    if len(A) == 2:
        return abs(A[0] - A[1])

    arr = []
    tmp1 = 0
    tmp2 = sum(A)
    for i in range(len(A) - 1):
        tmp1 = tmp1 + A[i]
        tmp2 = tmp2 - A[i]
        arr.append(abs(tmp1 - tmp2))

    return min(arr)