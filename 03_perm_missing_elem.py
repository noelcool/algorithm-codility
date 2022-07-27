

# write your code in Python 3.6
S = ["{", "[", "(", ")", "(", ")", "]", "}"]
if len(S) == 0:
    print(1)

arr = []
# 3 2 1 -1 1 -1 -2 -3
for i in S:
    if i == "{":
        arr.append(3)
    elif i == "[":
        arr.append(2)
    elif i == "(":
        arr.append(1)
    elif i == ")":
        arr.append(-1)
    elif i == "]":
        arr.append(-2)
    elif i == "}":
        arr.append(-3)


print(arr)
arr_ = arr
arr_ = []

for i in range(1, len(arr)):
    if len(arr_) != 0 and arr[i] < 0 and arr[i] == -1 * arr_[len(arr_) - 1]:
        del arr_[len(arr_) - 1]
    else:
        arr_.append(arr[i])

print(arr_)