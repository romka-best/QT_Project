def gen_cord():
    """Генератор всех возможных комбинаций координат"""
    all_comb = [[x / 10, x % 10] for x in range(100)]
    for_1_ship = filter(lambda x: x[0] in range(2, 8) and x[1] in range(2, 8), all_comb)
    for_other_ship = filter(lambda x: x not in for_1_ship, all_comb)
    cord_comb = {1: [[x] for x in for_1_ship], 2: [], 3: [], 4: []}
    for ship in filter(lambda x: x != 1, cord_comb.keys()):
        for cord in for_other_ship:
            hor_direction = [cord] + [[cord[0] + x, cord[1]] for x in range(1, ship)]
            ver_direction = [cord] + [[cord[0], cord[1] + x] for x in range(1, ship)]
            for dir_d in [hor_direction, ver_direction]:
                for cord_d in dir_d:
                    if cord_d not in for_other_ship:
                        break
                else:
                    cord_comb[ship].append(dir_d)
    return cord_comb


print(gen_cord())
