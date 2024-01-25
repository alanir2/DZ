from nim_game import get_bunches, put_stones, is_gameover, take_from_bunch

put_stones()
user_number = 1
while True:
    print('\033[92m' + 'Текущая позиция' + '\033[0m')
    print(get_bunches())
    # print('\033[0;35mХод игрока {}'.format(user_number)) if user_number == 1 else print(
    #     '\033[0;33mХод игрока {}'.format(user_number))
    print('Ход игрока {}'.format(user_number))
    pos = input('\033[0;36mОткуда берем ')
    qua = input('Сколько берем ')
    step_success = take_from_bunch(position=int(pos), quantity=int(qua))
    if step_success:
        user_number = 2 if user_number == 1 else 1
    else:
        print('no')
    if is_gameover:
        break
    user_number = 2 if user_number == 1 else 1

print('Выйграл игрок номер {}'.format(user_number))
