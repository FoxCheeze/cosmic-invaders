from game.physical_object import PhysicalObject


class Enemy(PhysicalObject):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def update(self, dt):
        super().update(dt)
