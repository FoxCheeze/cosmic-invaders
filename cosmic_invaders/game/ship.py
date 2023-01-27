import math

from game import resources, settings
from game.enemy import Enemy
from game.enemy_bullet import EnemyBullet
from game.player import Player
from game.player_bullet import PlayerBullet

from pyglet.math import Vec2
from pyglet.window import key


class Ship(Player):
    def __init__(self, *args, **kwargs):
        super().__init__(resources.player_image, *args, **kwargs)

        self.acceleration: float = 450
        self.bullet_speed: float = 500
        self.max_speed: int = 200
        self.rotation_speed: int = 350

    def update(self, dt):
        super().update(dt)

        if self.key_handler[key.A]:
            if self.velocity.x > -self.max_speed:
                self.velocity.x -= self.acceleration * dt

        elif self.key_handler[key.D]:
            if self.velocity.x < self.max_speed:
                self.velocity.x += self.acceleration * dt

        if self.key_handler[key.W]:
            if self.velocity.y < self.max_speed:
                self.velocity.y += self.acceleration * dt

        elif self.key_handler[key.S]:
            if self.velocity.y > -self.max_speed:
                self.velocity.y -= self.acceleration * dt

        if self.key_handler[key.LEFT]:
            self.rotation -= self.rotation_speed * dt
        if self.key_handler[key.RIGHT]:
            self.rotation += self.rotation_speed * dt

        self.wrap_in_window()

    def shoot(self):
        angle_radians: float = -math.radians(self.rotation)
        bullet_x: float = -math.sin(angle_radians)
        bullet_y: float = math.cos(angle_radians)
        bullet_direction: Vec2 = Vec2(bullet_x, bullet_y).normalize()

        bullet: PlayerBullet = PlayerBullet(
            direction=bullet_direction,
            speed=self.bullet_speed,
            x=self.x,
            y=self.y,
            batch=self.batch,
        )
        bullet.rotation = self.rotation

        settings.game_objects.append(bullet)
        resources.player_shoot.play()

    def on_key_press(self, symbol, _):
        if not self.dead:
            if symbol == key.SPACE:
                self.shoot()

            if symbol == key.UP:
                self.rotation += 180
            if symbol == key.DOWN:
                self.rotation += 180

    def on_collision(self, colliding_object):
        if issubclass(type(colliding_object), Enemy):
            self.take_damage()

        elif type(colliding_object) == EnemyBullet:
            self.take_damage()

    def take_damage(self):
        resources.player_hit.play()
        self.die()
