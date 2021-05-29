# Защита входных данных от вылета

def defend_game_number(input_args):
    """Защита от вылета при вводе номера раунда"""
    if input_args.isdigit() == 0:
        print("Введите число, а не строку!")
        return 0
    else:
        input_args = int(input_args)
        if input_args > 30 or input_args < 1:
            print("Номера игры от 1 до 30! Попробуйте еще раз")
            return 0


def defend_gamer_number(input_args):
    if input_args.isdigit() == 0:
        print("Введите число, а не строку!")
        return 0
    else:
        input_args = int(input_args)
        if input_args > 6 or input_args < 2:
            print("Номера игры от 1 до 30! Попробуйте еще раз")
            return 0
