def solution(S):
    if len(S) == 0:
        return 1
    if len(S) == 1 or len(S) % 2 == 1:
        return 0

    arr = []
    for i in range(len(S)):
        if S[i] == '(':
            arr.append(S[i])
        else: # ')'
            if len(arr) != 0 and arr[-1] == '(':
                arr.pop()
            else:
                arr.append(S[i])

    if len(arr) == 0:
        return 1
    return 0
    pass