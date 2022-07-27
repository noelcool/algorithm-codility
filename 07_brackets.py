def solution(S):
    # write your code in Python 3.6
    if len(S) == 0:
        return 1

    if len(S) == 1:
        return 0

    stack = []
    for i in range(0, len(S)):
        if S[i] == "(" or S[i] == "{" or S[i] == "[":
            stack.append(S[i])
        else:
            if len(stack) == 0:
                return 0
            last = stack.pop()
            if S[i] == ")" and last != "(":
                return 0
            elif S[i] == "}" and last != "{":
                return 0
            elif S[i] == "]" and last != "[":
                return 0

    if len(stack) != 0:
        return 0

    return 1