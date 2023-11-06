N = int(input("Кол-во чисел: "))

arr = []
for i in range(N):
    arr.append(int(input()))
napr = str(input("Направление сортировки (по возрастанию/по убыванию)? "))
print(arr)

if (napr == "по возрастанию"):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
elif (napr == "по убыванию"):
    for i in range(N - 1):
        for j in range(N - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
