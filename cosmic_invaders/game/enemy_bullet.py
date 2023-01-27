from game import resources
from pyglet.math import Vec2
from game.bullet import Bullet
from game.player import Player


class EnemyBullet(Bullet):
    def __init__(self, direction: Vec2, speed: float, *args, **kargs):
        super().__init__(
            img=resources.enemy_bullet,
            direction=direction,
            speed=speed,
            *args,
            **kargs
        )

    def update(self, dt):
        super().update(dt)

    def on_collision(self, colliding_object):
        if type(colliding_object) == Player:
            self.die()
