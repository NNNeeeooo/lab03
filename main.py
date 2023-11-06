N = int(input("Кол-во чисел: "))

arr = []
for i in range(N):
    arr.append(int(input()))
print(arr)

for i in range(N - 1):
    for j in range(N - i - 1):
        if arr[j] > arr[j + 1]:
           arr[j], arr[j + 1] = arr[j + 1], arr[j]

print(arr)
