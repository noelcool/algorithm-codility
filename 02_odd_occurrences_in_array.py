# 짝이 아닌 것 찾기

A = [9, 3, 9, 3, 9, 7, 9]

dict_ = {}

for i in A:
    if i in dict_.keys():
        dict_[i] += 1
    else:
        dict_[i] = 1

for k, v in dict_.items():
    if v % 2 == 1:
        print(k)
