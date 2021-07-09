if __name__ == '__main__' :
    n = int(input())
    for i in range(n):
        m = int(input())
        before = list(input().split())
        after = list(input().split())

        after.sort()
        before.sort()
        cnt = 0
        for j in range(m):
            if before[j] == after[j]:
                cnt += 1
        if cnt == m:
            print("NOT CHEATER")
        else:
            print("CHEATER")

