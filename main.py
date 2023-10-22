GAMES_CNT = 30

def fun_first(rock, scissors, paper):
    # Зафиксируем все наши 30 действий, как обратный жест
    # (жесту с максимальным кол-вом выбрасыванием у соперника)(1 случай)
    if rock == max(rock, scissors, paper):
        return [0, 0, GAMES_CNT]
    elif scissors == max(rock, scissors, paper):
        return [GAMES_CNT, 0, 0]
    return [0, GAMES_CNT, 0]


def fun_second(rock, scissors, paper):
    # Будем фиксировать жесты в пропорции(2 случай)
    return [paper, rock, scissors]


def cmp_functions(rock, scissors, paper):
    fir = fun_first(rock, scissors, paper)
    defeat_fir = round((fir[0] * paper + fir[1] * rock + fir[2] * scissors) / (GAMES_CNT * GAMES_CNT), 4)
    wins_fir = round((fir[0] * scissors + fir[1] * paper + fir[2] * rock) / (GAMES_CNT * GAMES_CNT), 4)
    draw_fir = round(1 - wins_fir - defeat_fir, 4)
    math_expect_1 = wins_fir - defeat_fir

    sec = fun_second(rock, scissors, paper)
    wins_sec = round((sec[0] * paper + sec[1] * rock + sec[2] * scissors) / (GAMES_CNT * GAMES_CNT), 4)
    defeat_sec = round((sec[0] * scissors + sec[1] * paper + sec[2] * rock) / (GAMES_CNT * GAMES_CNT), 4)
    draw_sec = round(1 - wins_sec - defeat_sec, 4)
    math_expect_2 = wins_sec - defeat_sec

    if max(math_expect_1, math_expect_2) == math_expect_1:
        return [1, round(math_expect_1 * 30, 4)]
    else:
        return [2, round(math_expect_2 * 30, 4)]


cnt = 0
for r in range(GAMES_CNT + 1):
    for s in range(GAMES_CNT + 1):
        for p in range(GAMES_CNT + 1):
            if r + s + p == GAMES_CNT:
                cnt += 1
                strategy_number, aver_win = cmp_functions(r, s, p)
                print(f'''При γК = {r}; γН = {s} γБ = {p}; Средний выигрыш(колво партий) используя стратегию № {strategy_number} = {aver_win}''')


print(f'''Количество различных комбинаций параметров: {cnt}''')

