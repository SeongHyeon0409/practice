T = int(input())

for _ in range(T):
    n, m, k = map(int, input().split())
    deck = [i for i in range(1, i+1)]
    card = list(map(int, input().split()))

    # 연속된 숫자들끼리 그룹
    # 그룹 중 가장 작은 숫자의 합
    # k번 반복

    # 가장작은 그룹 중 왼족에 붙이는게 이득?
    # 1 45 89 1 4 8
    # 1 4 7

    1 4 6 9

    1 4 5 6 9

    1 4 5 6 89
    1 4 8

    1 4  6 7 9
    1 4  6 7 8 9
    1 4 6

    1 4 9

    1 3 9

    # 몇 번 반복하냐에 따라 최적의 점수가 달라짐.;