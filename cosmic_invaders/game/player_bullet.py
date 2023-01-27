from game import resources
from pyglet.math import Vec2
from game.bullet import Bullet
from game.enemy import Enemy


class PlayerBullet(Bullet):
    def __init__(self, direction: Vec2, speed: float, *args, **kargs):
        super().__init__(
            img=resources.player_bullet,
            direction=direction,
            speed=speed,
            *args,
            **kargs
        )

    def update(self, dt):
        super().update(dt)

    def on_collision(self, colliding_object):
        if issubclass(type(colliding_object), Enemy):
            self.die()
