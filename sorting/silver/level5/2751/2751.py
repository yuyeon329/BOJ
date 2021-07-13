import sys
if __name__ == '__main__':
    arr = []
    n = int(input())
    for _ in range(n):
        arr.append(int(sys.stdin.readline()))
    for i in sorted(arr):
        sys.stdout.write(str(i)+'\n')