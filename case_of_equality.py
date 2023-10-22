GAMES_CNT = 30
fir = [10, 10, 10]


def cmp_functions(rock, scissors, paper):
    wins_fir = round((fir[0] * paper + fir[1] * rock + fir[2] * scissors) / (GAMES_CNT * GAMES_CNT), 4)
    defeat_fir = round((fir[0] * scissors + fir[1] * paper + fir[2] * rock) / (GAMES_CNT * GAMES_CNT), 4)
    draw_fir = round(1 - wins_fir - defeat_fir, 4)
    math_expect_1 = wins_fir - defeat_fir

    return math_expect_1


print("если у нашего соперника γК = γН = γБ = 10")
cnt = 0
for r in range(GAMES_CNT + 1):
    for s in range(GAMES_CNT + 1):
        for p in range(GAMES_CNT + 1):
            if r + s + p == GAMES_CNT:
                cnt += 1
                aver_win = cmp_functions(r, s, p)
                print(f'''Используя наши параметры К = {r}; Н = {s} Б = {p}; Средний выигрыш(колво партий) = {aver_win}''')


print(f'''Количество различных комбинаций параметров: {cnt}''')

