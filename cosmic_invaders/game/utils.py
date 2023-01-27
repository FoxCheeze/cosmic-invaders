from game import enemy, ship


def no_enemies_in(objects: list) -> bool:
    for object in objects:
        if issubclass(type(object), enemy.Enemy):
            return False

    return True


def player_alive_in(objects: list) -> bool:
    for object in objects:
        if type(object) == ship.Ship:
            return True

    return False
