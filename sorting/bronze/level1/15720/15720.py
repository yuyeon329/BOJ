if __name__ == '__main__':
    burger, side, drink = map(int, input().split())
    b = sorted(list(map(int, input().split())), reverse=True)
    s = sorted(list(map(int, input().split())), reverse=True)
    d = sorted(list(map(int, input().split())), reverse=True)

    org = sum(b) + sum(s) + sum(d)
    dcnt = 0
    set_n = min(burger, side, drink)

    for i in range(set_n):
        dcnt += (b[i] + s[i] + d[i])*0.1

    print(org)
    print(int(org - dcnt))
