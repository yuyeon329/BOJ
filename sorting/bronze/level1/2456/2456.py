if __name__ == '__main__':
    num = int(input())
    score = [0]*3
    power_score = [0]*3

    for i in range(num):
        one, two, three = map(int, input().split())
        score[0] += one
        score[1] += two
        score[2] += three

        power_score[0] += one**2
        power_score[1] += two**2
        power_score[2] += three**2

    max_score = max(score)

    if score.count(max(score)) == 1:
        for i in range(3):
            if score[i] == max_score:
                print(i + 1, score[i])
                break
    else:
        max_power_score = max(power_score)
        if power_score.count(max(power_score)) == 1:
            for i in range(3):
                if power_score[i] == max_power_score:
                    print(i+1, score[i])

        else:
            print(0, max(score))
