from random import randint

_holder = {}
max_bunxhes = 3
max_bunxhes_size = 10
_sorted_keys = None


def put_stones():
    global _holder, _sorted_keys
    _holder = {}
    for i in range(1, max_bunxhes + 1):
        _holder[i] = randint(1, max_bunxhes_size)
    _sorted_keys = sorted(_holder.keys())


def take_from_bunch(position, quantity):
    if position in _holder:
        _holder[position] -= quantity
        return True
    else:
        return False


def get_bunches():
    res = []
    for key in _sorted_keys:
        res.append(_holder[key])
    return res


def is_gameover():
    return sum(_holder.values()) == 0
