arr, arr_w, arr_k = [], [], []

for _ in range(20):
    arr.append(int(input()))

arr_w = arr[:10]
arr_k = arr[10:]

arr_w.sort(reverse=True)
arr_k.sort(reverse=True)

print(arr_w[0]+arr_w[1]+arr_w[2], arr_k[0]+arr_k[1]+arr_k[2],end="")
