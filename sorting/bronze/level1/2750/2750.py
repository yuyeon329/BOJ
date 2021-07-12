def heap_sort(unsorted):
    n = len(unsorted)
    for i in range(1, n):
        child = i
        while child != 0:
            parent = (child-1)//2
            if unsorted[parent] > unsorted[child]:
                unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]
            child = parent

    for node in range(n-1, -1, -1):
        unsorted[0], unsorted[node] = unsorted[node], unsorted[0]
        parent = 0
        child = 1

        while child < node:
            child = parent*2 + 1
            if child < node-1 and unsorted[child] > unsorted[child+1]:
                child += 1
            if child < node and unsorted[parent] > unsorted[child]:
                unsorted[parent], unsorted[child] = unsorted[child], unsorted[parent]

            parent = child
        print(unsorted[node])
    return 0

if __name__ == '__main__' :
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(int(input()))
    heap_sort(arr)