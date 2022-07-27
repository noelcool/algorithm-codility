
X = 10
Y = 85
D = 30


def solution(X, Y, D):
    """
    X + a * D >= Y
    a * D >= Y - X
    a >= (Y - X) / D
    """
    res = (Y - X) / D
    if res % 1 == 0:
        return int(res)
    else:
        return int(res) + 1


print(solution(X, Y, D))