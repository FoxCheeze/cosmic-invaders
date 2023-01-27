import math
import random

from game import resources, settings
from game.enemy_bullet import EnemyBullet
from game.invader import Invader
from pyglet.math import Vec2


class InvaderAlien(Invader):
    def __init__(self, *args, **kwargs):
        super().__init__(resources.invader_alien, *args, **kwargs)

        self.max_speed: int = 150
        self.speed: Vec2 = Vec2(
            random.randint(-self.max_speed, self.max_speed),
            random.randint(-self.max_speed, self.max_speed),
        )

        self.scale = 2
        self.bullet_speed = 400
        self.score_value = 500

    def update(self, dt):
        super().update(dt)

        self.velocity.x = self.speed.x
        self.velocity.y = self.speed.y

        if random.randint(0, 100) == 0:
            self.shoot()

        self.wrap_in_window()

    def shoot(self):
        rotation = random.randint(0, 1000)
        angle_radians: float = -math.radians(rotation)
        bullet_x: float = -math.sin(angle_radians)
        bullet_y: float = math.cos(angle_radians)
        bullet_direction: Vec2 = Vec2(bullet_x, bullet_y).normalize()

        bullet: EnemyBullet = EnemyBullet(
            direction=bullet_direction,
            speed=self.bullet_speed,
            x=self.x,
            y=self.y,
            batch=self.batch,
        )
        bullet.rotation = rotation
        bullet.scale = 1.2

        settings.game_objects.append(bullet)
        resources.enemy_shoot.play()
