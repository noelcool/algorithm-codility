# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    block_cnt = 0
    stack_arr = []

    for i in range(len(H)):
        while len(stack_arr) > 0 and stack_arr[-1] > H[i]:
            stack_arr.pop()

        if len(stack_arr) == 0 or stack_arr[-1] < H[i]:
            block_cnt += 1
            stack_arr.append(H[i])

    return block_cnt
