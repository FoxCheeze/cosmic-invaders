import math
import random

from game import resources, settings
from game.enemy_bullet import EnemyBullet
from game.invader import Invader
from game.invader_alien import InvaderAlien
from pyglet.math import Vec2


class InvaderShip(Invader):
    def __init__(self, *args, **kwargs):
        super().__init__(resources.invader_ship_image, *args, **kwargs)

        self.max_speed: int = 200
        self.speed: Vec2 = Vec2(
            random.randint(-self.max_speed, self.max_speed),
            random.randint(-self.max_speed, self.max_speed),
        )

        self.bullet_speed = 300
        self.scale = 4
        self.score_value = 250

    def update(self, dt):
        super().update(dt)

        self.velocity.x = self.speed.x
        self.velocity.y = self.speed.y

        if random.randint(0, 175) == 0:
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
        bullet.scale = 1.8

        settings.game_objects.append(bullet)
        resources.enemy_shoot.play()

    def on_death(self):
        super().on_death()

        new_invader1: InvaderAlien = InvaderAlien(
            x=self.x - 10, y=self.y, batch=self.batch
        )
        new_invader2: InvaderAlien = InvaderAlien(
            x=self.x + 10, y=self.y, batch=self.batch
        )

        settings.game_objects.append(new_invader1)
        settings.game_objects.append(new_invader2)
