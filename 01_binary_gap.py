num = bin(39)
arr_ = []
print(num)

for i in range(0, len(num)):
    if num[i] == '1':
        arr_.append(i)

arr2_ = []
for i in range(0, len(arr_)):
    if i != len(arr_) - 1:
        tmp = arr_[i+1] - arr_[i]
        print(arr_[i+1], arr_[i])
        arr2_.append(tmp)

if len(arr2_) == 0:
    print(0)
else:
    print(max(arr2_))

