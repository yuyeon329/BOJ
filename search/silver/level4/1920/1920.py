def binary_search(arr_n, target):
    l, r = 0, len(arr_n)-1
    while l <= r:
        m = (l + r) // 2
        if target == arr_n[m]:
            return 1
        elif target < arr_n[m]:
            r = m - 1
        else :
            l = m + 1
    return 0

if __name__ == '__main__':
    n = int(input())
    arr_n = list(map(int, input().split()))
    m = int(input())
    arr_m = list(map(int, input().split()))

    arr_n.sort()
    for i in arr_m:
        if binary_search(arr_n, i):
            print(1)
        else:
            print(0)
