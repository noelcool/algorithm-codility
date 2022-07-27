def solution(A, B):
    if len(A) == 0:
        return 0
    if len(A) == 1:
        return 1

    down = []
    up = 0
    for i in range(0, len(A)):
        if B[i] == 1:  # 내려감
            down.append(A[i])
        else:  # 올라감
            while True:
                if len(down) == 0:
                    break
                last = down[-1]
                if last > A[i]:
                    break
                else:
                    down.pop()
            if len(down) == 0:
                up += 1

    return up + len(down)