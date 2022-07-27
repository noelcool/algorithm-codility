# 한 칸씩 오른쪽으로 쉬프트

input_list = [3, 8, 9, 7, 6]
k = 3
arr_ = list(range(len(input_list)))
for i in range(len(input_list)):
    arr_[(i+k) % len(input_list)] = input_list[i]
"""
3 8 9 7 6
8 9 7 6 3
9 7 6 3 8
                                                           3, 8, 9, 7, 6
                                                           0, 1, 2, 3, 4
arr_[(0+3) % 5] = input_list[0]    0 index val -> 3 index  0, 1, 2, 3, 4
arr_[(1+3) % 5] = input_list[1]    1 index val -> 4 index  0, 1, 2, 3, 8
arr_[(2+3) % 5] = input_list[2]    2 index val -> 0 index  9, 1, 2, 3, 8
arr_[(3+3) % 5] = input_list[3]    3 index val -> 1 index  9, 7, 2, 3, 8
arr_[(4+3) % 5] = input_list[4]    4 index val -> 2 index  9, 7, 6, 3, 8
"""
print(arr_)  # [9, 7, 6, 3, 8]