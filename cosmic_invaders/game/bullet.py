from pyglet.math import Vec2
from game.physical_object import PhysicalObject


class Bullet(PhysicalObject):
    def __init__(self, direction: Vec2, speed: float, *args, **kargs):
        super().__init__(*args, **kargs)

        self.speed: float = speed
        self.direction: Vec2 = direction

    def update(self, dt):
        super().update(dt)

        self.velocity = self.direction * self.speed

        # Delete if out of the window
        if not self.is_on_window():
            self.dead = True
